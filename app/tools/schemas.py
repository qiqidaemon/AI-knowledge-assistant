tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "获取指定时区的当前日期和时间",
            "parameters": {
                "type": "object",
                "properties": {
                    "timezone":{
                        "type":"string",
                        "description":(
                            "IANA 时区名词,例如"
                            "中国使用 Asia/Shanghai,"
                            "纽约使用 America/New_York,"
                            "东京使用 Asia/Tokyo"
                        )

                        
                    }
                },
                "required":["timezone"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "search_knowledge",
            "description": "当用户询问知识库中的专业知识、人物信息、项目文档等内容时，搜索知识库",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "需要在知识库中搜索的问题"
                    }
                },
                "required": ["query"]
            }
        }
    }
]