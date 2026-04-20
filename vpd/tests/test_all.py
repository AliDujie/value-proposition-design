import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from vpd import (
    InterviewGenerator, InterviewConfig,
    SurveyDesigner, SurveyConfig, SurveyHypothesis,
    PriorityCalculator, CanvasAnalyzer, StrategyScorer,
    SampleCalculator, ExperimentDesigner,
)


def test_interview_generator_b2c():
    ig = InterviewGenerator()
    cfg = ig.configure(
        business_scenario="飞猪国内酒店预订",
        target_customer="25-35岁商旅用户",
        duration_minutes=45,
        customer_type="B2C",
        stage="探索期",
    )
    assert cfg.business_scenario == "飞猪国内酒店预订"
    info = ig.generate()
    assert info["total_questions"] == 25
    assert info["is_b2b"] is False
    assert info["recommended_interviewees"] >= 10
    assert info["stage_goal"] == "发现客户的工作、痛点和收益（开放式）"
    md = ig.render_markdown()
    assert "阶段一：暖场与背景" in md
    assert "阶段二：工作探索" in md
    assert "阶段三：痛点挖掘" in md
    assert "阶段四：收益发现" in md
    assert "阶段五：收尾与拓展" in md
    assert "八大原则" in md
    assert "飞猪国内酒店预订" in md
    assert "B2B多角色" not in md
    print("✅ InterviewGenerator (B2C) passed")


def test_interview_generator_b2b():
    ig = InterviewGenerator()
    ig.configure(
        business_scenario="企业级SaaS采购",
        target_customer="中型企业IT负责人",
        known_hypotheses=["用户最大痛点是集成困难", "决策周期超过3个月"],
        duration_minutes=60,
        customer_type="B2B",
        stage="验证期",
    )
    info = ig.generate()
    assert info["is_b2b"] is True
    assert info["has_hypotheses"] is True
    assert info["hypotheses_count"] == 2
    assert len(info["b2b_roles"]) == 4
    md = ig.render_markdown()
    assert "B2B多角色版本提纲要点" in md
    assert "最终用户" in md
    assert "经济购买者" in md
    assert "决策者" in md
    assert "影响者/建议者" in md
    assert "已知假设验证追问" in md
    assert "集成困难" in md
    print("✅ InterviewGenerator (B2B) passed")


def test_interview_generator_validation():
    ig = InterviewGenerator()
    try:
        ig.configure("场景", "客户", customer_type="INVALID")
        assert False, "should raise"
    except ValueError:
        pass
    try:
        ig.configure("场景", "客户", stage="无效阶段")
        assert False, "should raise"
    except ValueError:
        pass
    try:
        ig.configure("场景", "客户", duration_minutes=5)
        assert False, "should raise"
    except ValueError:
        pass
    print("✅ InterviewGenerator validation passed")


def test_survey_designer_basic():
    sd = SurveyDesigner()
    sd.configure(
        business_scenario="飞猪国内酒店预订",
        target_customer="25-35岁商旅用户",
        hypotheses=[
            {"description": "用户最大痛点是价格不透明", "category": "customer_profile"},
            {"description": "用户愿意为无忧退改额外付费", "category": "value_proposition"},
        ],
        survey_type="客户概况验证",
        target_sample_size=200,
        channel="线上",
    )
    sd.set_jobs(["预订酒店", "比价", "查看评价", "办理入住"])
    sd.set_pains(["价格不透明", "退改困难", "房型描述不准确"])
    sd.set_gains(["一键预订省时间", "获得专属优惠", "无忧退改"])
    info = sd.generate()
    assert info["hypotheses_count"] == 2
    assert info["estimated_questions"] > 10
    assert info["min_sample_size_95"] == 385
    assert "筛选题" in info["parts"]
    assert "痛点严重度评估" in info["parts"]
    md = sd.render_markdown()
    assert "Part 1：筛选题" in md
    assert "Part 2：客户工作重要性评估" in md
    assert "Part 3：痛点严重度评估" in md
    assert "Part 4：收益期望评估" in md
    assert "Part 6：人口统计学信息" in md
    assert "数据分析建议" in md
    assert "价格不透明" in md
    assert "李克特量表" in md
    assert "假设验证对照表" in md
    print("✅ SurveyDesigner (basic) passed")


def test_survey_designer_with_vp():
    sd = SurveyDesigner()
    sd.configure(
        business_scenario="在线教育平台",
        target_customer="职场新人",
        hypotheses=["用户希望获得实战项目经验"],
        survey_type="价值主张验证",
    )
    sd.set_jobs(["学习新技能", "获取证书"])
    sd.set_pains(["课程质量参差不齐", "学完无法实践"])
    sd.set_gains(["快速上手新技能", "获得行业认可"])
    sd.set_value_propositions(["提供真实企业项目实战", "AI导师1对1辅导"])
    sd.set_alternatives(["B站免费课程", "线下培训班"])
    info = sd.generate()
    assert info["has_value_propositions"] is True
    assert "价值主张验证" in info["parts"]
    md = sd.render_markdown()
    assert "Part 5：价值主张验证" in md
    assert "方案A" in md
    assert "方案B" in md
    assert "B站免费课程" in md
    print("✅ SurveyDesigner (with VP & alternatives) passed")


def test_survey_designer_validation():
    sd = SurveyDesigner()
    try:
        sd.configure("场景", "客户", hypotheses=[], survey_type="客户概况验证")
        assert False, "should raise"
    except ValueError:
        pass
    try:
        sd.configure("场景", "客户", hypotheses=["假设1"], survey_type="无效类型")
        assert False, "should raise"
    except ValueError:
        pass
    try:
        sd.configure("场景", "客户", hypotheses=["假设1"], channel="无效渠道")
        assert False, "should raise"
    except ValueError:
        pass
    print("✅ SurveyDesigner validation passed")


def test_priority_calculator():
    calc = PriorityCalculator()
    calc.add_item("价格不透明", importance=5, dissatisfaction=5, frequency=4, viability=4)
    calc.add_item("退改困难", importance=4, dissatisfaction=4, frequency=3, viability=3)
    calc.add_item("客服响应慢", importance=3, dissatisfaction=3, frequency=5, viability=5)
    ranked = calc.rank()
    assert len(ranked) == 3
    assert ranked[0]["name"] == "价格不透明"
    assert ranked[0]["normalized_score"] == round(5*5*4*4/625*100, 1)
    assert ranked[0]["grade"] in ("P0", "P1", "P2", "P3")
    md = calc.render_markdown(title="测试矩阵", evaluation_type="痛点")
    assert "价格不透明" in md
    assert "P0" in md or "P1" in md
    print("✅ PriorityCalculator passed")


def test_priority_with_competition():
    calc = PriorityCalculator()
    calc.add_item("A", 5, 5, 5, 5, competition_coverage="not_covered")
    calc.add_item("B", 5, 5, 5, 5, competition_coverage="fully_covered")
    ranked = calc.rank()
    assert ranked[0]["name"] == "A"
    assert ranked[0]["final_score"] > ranked[1]["final_score"]
    print("✅ PriorityCalculator with competition passed")


def test_canvas_analyzer():
    ca = CanvasAnalyzer()
    ca.customer_name = "亲子家庭用户"
    ca.product_name = "飞猪酒店预订"
    ca.add_job("预订合适的家庭房", "functional", 5)
    ca.add_job("让家人觉得安排周到", "social", 4)
    ca.add_pain("价格不透明", "critical", "比其他平台贵10%以上")
    ca.add_pain("退改困难", "severe")
    ca.add_gain("一键预订省时间", "required")
    ca.add_gain("获得专属优惠", "desired")
    ca.add_product("智能比价引擎", "digital")
    ca.add_pain_reliever("实时比价展示", "价格不透明", "full")
    ca.add_pain_reliever("灵活退改政策", "退改困难", "partial")
    ca.add_gain_creator("一键下单功能", "一键预订省时间", "full")
    fit = ca.analyze_fit()
    assert 0 <= fit["overall_score"] <= 100
    assert fit["pain_coverage"]["full"] == 1
    assert fit["pain_coverage"]["partial"] == 1
    assert fit["gain_coverage"]["uncovered"] == 1
    md = ca.render_markdown()
    assert "契合度" in md
    print(f"✅ CanvasAnalyzer passed (score={fit['overall_score']})")


def test_strategy_scorer():
    ss = StrategyScorer()
    ss.set_factors(["价格", "品质", "速度", "服务", "个性化"])
    ss.add_player("我方", [7, 8, 5, 6, 4])
    ss.add_player("竞品A", [8, 6, 7, 5, 3])
    ss.add_player("竞品B", [6, 7, 8, 4, 2])
    result = ss.analyze("我方")
    assert len(result["factor_analysis"]) == 5
    assert isinstance(result["advantages"], list)
    md = ss.render_markdown("我方")
    assert "蓝海" in md
    print("✅ StrategyScorer passed")


def test_sample_calculator():
    sc = SampleCalculator()
    r = sc.minimum_sample_size(confidence=95, margin_of_error=0.05)
    assert r["sample_size"] == 385
    r2 = sc.minimum_sample_size(confidence=95, margin_of_error=0.05, population=1000)
    assert r2["sample_size"] < 385
    md = sc.render_markdown()
    assert "385" in md
    print(f"✅ SampleCalculator passed (n={r['sample_size']}, n_adj={r2['sample_size']})")


def test_experiment_designer():
    ed = ExperimentDesigner()
    ed.add_hypothesis("用户愿意为无忧退改额外付费30元", lethality="lethal", evidence_strength="none")
    ed.add_hypothesis("用户最大痛点是价格不透明", lethality="important", evidence_strength="weak")
    ranked = ed.rank_hypotheses()
    assert ranked[0]["lethality"] == "🔴 致命"
    ed.create_test_card(
        hypothesis="用户愿意为无忧退改额外付费30元",
        test_method="登录页MVP",
        metric="点击率",
        threshold="5%",
        falsification="点击率<2%则否定",
        cta_level="L3",
        duration_days=14,
        sample_size=200,
    )
    methods = ed.suggest_method(budget="low")
    assert len(methods) > 0
    irl = ed.investment_readiness_level(3, 10)
    assert irl["level"] >= 1
    md = ed.render_markdown()
    assert "测试卡" in md
    print("✅ ExperimentDesigner passed")


def test_vpd_skill_full_workflow():
    from vpd import VPDSkill
    skill = VPDSkill("飞猪国内酒店预订", "25-35岁商旅用户")
    assert skill.business_scenario == "飞猪国内酒店预订"
    assert skill.target_customer == "25-35岁商旅用户"

    interview_md = skill.generate_interview(stage="探索期")
    assert "阶段一：暖场与背景" in interview_md
    assert "飞猪国内酒店预订" in interview_md

    survey_md = skill.generate_survey(
        hypotheses=["用户最大痛点是价格不透明", "用户愿意为无忧退改额外付费"],
        jobs=["预订酒店", "比价", "查看评价"],
        pains=["价格不透明", "退改困难"],
        gains=["一键预订省时间", "获得专属优惠"],
    )
    assert "Part 1：筛选题" in survey_md
    assert "价格不透明" in survey_md

    priority_md = skill.calculate_priority([
        {"name": "价格不透明", "importance": 5, "dissatisfaction": 5, "frequency": 4, "viability": 4},
        {"name": "退改困难", "importance": 4, "dissatisfaction": 4, "frequency": 3, "viability": 3},
        {"name": "客服响应慢", "importance": 3, "dissatisfaction": 3, "frequency": 5, "viability": 5},
    ])
    assert "价格不透明" in priority_md
    assert "P0" in priority_md or "P1" in priority_md

    canvas_md = skill.analyze_canvas(
        product_name="飞猪酒店预订",
        jobs=[{"description": "预订合适的家庭房", "category": "functional", "importance": 5}],
        pains=[{"description": "价格不透明", "severity": "critical"}],
        gains=[{"description": "一键预订省时间", "desire_level": "required"}],
        products=[{"description": "智能比价引擎", "category": "digital"}],
        pain_relievers=[{"description": "实时比价展示", "target_pain": "价格不透明", "coverage": "full"}],
        gain_creators=[{"description": "一键下单功能", "target_gain": "一键预订省时间", "coverage": "full"}],
    )
    assert "契合度" in canvas_md

    competitor_md = skill.analyze_competitor(
        my_name="飞猪",
        factors=["价格", "品质", "速度", "服务"],
        players={"飞猪": [7, 8, 5, 6], "携程": [8, 7, 7, 5], "美团": [6, 6, 8, 4]},
    )
    assert "蓝海" in competitor_md
    assert "飞猪" in competitor_md

    experiment_md = skill.design_experiment(
        hypotheses=[
            {"description": "用户愿意为无忧退改额外付费30元", "lethality": "lethal"},
            {"description": "用户最大痛点是价格不透明", "lethality": "important", "evidence_strength": "weak"},
        ],
        test_cards=[{
            "hypothesis": "用户愿意为无忧退改额外付费30元",
            "test_method": "登录页MVP",
            "metric": "点击率",
            "threshold": "5%",
            "falsification": "点击率<2%则否定",
            "cta_level": "L3",
        }],
    )
    assert "测试卡" in experiment_md

    sample_md = skill.calculate_sample_size(confidence=95, margin_of_error=0.05)
    assert "385" in sample_md

    s = skill.summary()
    assert s["modules_count"] == 7
    assert "interview" in s["modules_executed"]
    assert "canvas" in s["modules_executed"]
    assert s["canvas_fit_score"] > 0
    assert s["top_priority"] == "价格不透明"
    assert s["hypotheses_count"] == 2
    assert s["test_cards_count"] == 1

    full_report = skill.render_all()
    assert "价值主张设计全景报告" in full_report
    assert "7 个分析模块" in full_report
    assert "阶段一：暖场与背景" in full_report
    assert "蓝海" in full_report
    print("✅ VPDSkill full workflow passed")


def test_vpd_skill_partial():
    from vpd import VPDSkill
    skill = VPDSkill("在线教育平台", "职场新人")
    md = skill.generate_interview(customer_type="B2C", duration_minutes=30)
    assert "在线教育平台" in md
    s = skill.summary()
    assert s["modules_count"] == 1
    assert s["modules_executed"] == ["interview"]
    report = skill.render_all()
    assert "1 个分析模块" in report
    print("✅ VPDSkill partial workflow passed")


if __name__ == "__main__":
    test_interview_generator_b2c()
    test_interview_generator_b2b()
    test_interview_generator_validation()
    test_survey_designer_basic()
    test_survey_designer_with_vp()
    test_survey_designer_validation()
    test_priority_calculator()
    test_priority_with_competition()
    test_canvas_analyzer()
    test_strategy_scorer()
    test_sample_calculator()
    test_experiment_designer()
    test_vpd_skill_full_workflow()
    test_vpd_skill_partial()
    print("\n🎉 All 14 tests passed! All 6 modules + VPDSkill verified!")
