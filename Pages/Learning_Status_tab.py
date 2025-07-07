from nicegui import app as nicegui_app, ui


def Learning_Status_tab():
    ui.label("On update")
    with ui.row():
        with ui.card().classes("fit").style("min-height: 500px;min-width:500px"):
            ui.echart(
                {
                    "title": {
                        "text": "Referer of a Website",
                        "subtext": "Fake Data",
                        "left": "center",
                    },
                    "legend": {
                        "data": [
                            "ATX Jeans",
                            "NEU Jacket",
                            "HUCE T Shirt",
                            "UEB Shoes",
                            "FTU Jacket",
                            "HUST Shirt",
                        ],
                        "orient": "vertical",
                        # "left": "left",
                        "type": "scroll",
                        "right": 0,
                        "top": 50,
                        "bottom": 20,
                    },
                    "xAxis": {
                        "type": "category",
                        "boundaryGap": "false",
                        "data": [
                            "2025-1",
                            "2025-2",
                            "2025-3",
                            "2025-4",
                            "2025-5",
                            "2025-6",
                        ],
                        "axisLabel": {"interval": 0, "rotate": 30},
                    },
                    "yAxis": {"type": "value"},
                    "series": [
                        {
                            "name": "ATX Jeans",
                            "data": [
                                3500000,
                                4500000,
                                4500000,
                                3750000,
                                4000000,
                                2500000,
                            ],
                            "type": "line",
                            "stack": "Total",
                            "areaStyle": {},
                            "emphasis": {"focus": "series"},
                            # "smooth": "true",
                        },
                        {
                            "name": "NEU Jacket",
                            "data": [
                                3500000,
                                4500000,
                                4500000,
                                3750000,
                                4000000,
                                2500000,
                            ],
                            "type": "line",
                            "stack": "Total",
                            "areaStyle": {},
                            "emphasis": {"focus": "series"},
                            # "smooth": "true",
                        },
                        {
                            "name": "HUCE T Shirt",
                            "data": [
                                3500000,
                                4500000,
                                4500000,
                                3750000,
                                4000000,
                                2500000,
                            ],
                            "type": "line",
                            "stack": "Total",
                            "areaStyle": {},
                            "emphasis": {"focus": "series"},
                            # "smooth": "true",
                        },
                        {
                            "name": "UEB Shoes",
                            "data": [
                                3500000,
                                4500000,
                                4500000,
                                3750000,
                                4000000,
                                2500000,
                            ],
                            "type": "line",
                            "stack": "Total",
                            "areaStyle": {},
                            "emphasis": {"focus": "series"},
                            # "smooth": "true",
                        },
                        {
                            "name": "FTU Jacket",
                            "data": [
                                3500000,
                                4500000,
                                4500000,
                                3750000,
                                4000000,
                                2500000,
                            ],
                            "type": "line",
                            "stack": "Total",
                            "areaStyle": {},
                            "emphasis": {"focus": "series"},
                            # "smooth": "true",
                        },
                        {
                            "name": "HUST Shirt",
                            "data": [
                                3500000,
                                4500000,
                                4500000,
                                3750000,
                                4000000,
                                2500000,
                            ],
                            "type": "line",
                            "stack": "Total",
                            "areaStyle": {},
                            "emphasis": {"focus": "series"},
                            # "smooth": "true",
                        },
                    ],
                    "textStyle": {"fontFamily": "consolas"},
                    "tooltip": {
                        "trigger": "axis",
                        "axisPointer": {
                            "type": "cross",  # cross
                            "label": {"backgroundColor": "#6a7985"},
                        },
                    },
                    "grid": {
                        "left": "3%",
                        "right": "4%",
                        "bottom": "3%",
                        "containLabel": "true",
                    },
                    "toolbox": {"feature": {"saveAsImage": {}}},
                }
            ).style("min-height: 500px;min-width:500px")
        with ui.card().classes("fit").style("min-height: 500px;min-width:500px"):
            ui.echart(
                {
                    "title": {
                        "text": "Referer of a Website",
                        "subtext": "Fake Data",
                        "left": "center",
                    },
                    "tooltip": {"trigger": "item"},
                    "legend": {"orient": "vertical", "left": "left"},
                    "series": [
                        {
                            "name": "Access From",
                            "type": "pie",
                            "radius": "50%",
                            "data": [
                                {"value": 1048, "name": "Search Engine"},
                                {"value": 735, "name": "Direct"},
                                {"value": 580, "name": "Email"},
                                {"value": 484, "name": "Union Ads"},
                                {"value": 300, "name": "Video Ads"},
                            ],
                            "emphasis": {
                                "itemStyle": {
                                    "shadowBlur": 10,
                                    "shadowOffsetX": 0,
                                    "shadowColor": "rgba(0, 0, 0, 0.5)",
                                }
                            },
                        }
                    ],
                }
            ).style("min-height: 500px;min-width:500px")
