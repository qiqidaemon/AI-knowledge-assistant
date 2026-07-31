# 🤖 AI Knowledge Assistant

基于 **FastAPI + DeepSeek LLM + Redis + PostgreSQL** 构建的智能知识助手后端系统。

该项目实现了一个面向实际应用场景的 AI 对话系统，支持：

- 大语言模型对话
- 流式响应输出
- 多轮上下文记忆
- Redis 短期记忆管理
- PostgreSQL 长期数据持久化
- 会话管理
- RESTful API 服务


---

# 📌 项目简介

随着大语言模型（LLM）的快速发展，AI 应用不仅需要调用模型生成文本，还需要解决：

- 如何管理用户多轮对话？
- 如何保存聊天历史？
- 如何控制上下文长度？
- 如何设计可扩展的 AI 服务架构？

本项目基于 FastAPI 构建 AI 对话后端，通过 Redis 管理短期上下文，通过 PostgreSQL 保存长期聊天记录，实现一个具备记忆能力的 AI Assistant。


---

# ✨ 核心功能


## 1. LLM 对话能力

集成 DeepSeek 大语言模型 API，实现智能问答。

支持：

- 用户问题理解
- AI 自动生成回复
- Streaming 流式输出


用户发送：
你好


模型实时返回：


你好！有什么可以帮助你的吗？



---

## 2. 多轮对话记忆

系统支持基于 conversation_id 的上下文管理。


示例：


用户：
我叫 Tom

AI：
你好 Tom，很高兴认识你。

用户：
我的名字是什么？

AI：
你的名字是 Tom。



通过保存历史消息，使模型能够理解上下文。


---

## 3. Redis 短期记忆


使用 Redis 保存最近对话上下文。


作用：

- 快速读取聊天历史
- 提供 LLM 上下文
- 限制上下文窗口大小
- 支持 TTL 自动过期


数据结构：


conversation_id

    |
    |
  Redis

    |
    |

最近 N 轮聊天记录



---

## 4. PostgreSQL 长期消息存储


使用 PostgreSQL 保存完整聊天记录。


存储内容：

- conversation_id
- 用户/AI角色
- 消息内容
- 创建时间


数据库结构：

|字段|说明|
|-|-|
|id|消息ID|
|conversation_id|会话ID|
|role|消息角色|
|content|消息内容|
|created_at|创建时间|



---

# 🏗 系统架构


             用户

              |

              |

          FastAPI

              |

    ---------------------

    |                   |

  Redis            PostgreSQL

短期上下文 长期存储

    |

    |

   LLM

    |

    |

Streaming Response



---

# 🛠 技术栈


## 后端

- Python
- FastAPI
- Uvicorn


## 大语言模型

- DeepSeek API
- OpenAI Compatible SDK


## 数据存储

- Redis
- PostgreSQL
- SQLAlchemy


## 工程化

- Docker
- Git


---

# 📂 项目结构



AI-knowledge-assistant

├── app
│
├── api
│ ├── chat.py
│ └── conversation.py
│
├── core
│ ├── config.py
│ ├── database.py
│ ├── redis.py
│ └── logger.py
│
├── models
│ └── message.py
│
├── services
│ ├── llm.py
│ ├── memory.py
│ └── db_service.py
│
└── main.py



---

# ⚙️ 环境配置


## 1. 克隆项目


```bash
git clone https://github.com/qiqidaemon/AI-knowledge-assistant.git

cd AI-knowledge-assistant
2. 创建虚拟环境
python -m venv .venv

激活：

Windows:

.venv\Scripts\activate
3. 安装依赖
pip install -r requirements.txt
4. 配置环境变量

创建 .env 文件：

DEEPSEEK_API_KEY=your_api_key

MODEL_NAME=deepseek-chat

REDIS_HOST=localhost

REDIS_PORT=6379

DATABASE_URL=postgresql://admin:123456@localhost:5432/ai_assistant

🚀 启动项目

启动 Redis：

docker start redis-chat

启动 PostgreSQL：

docker start postgres-ai

启动服务：

uvicorn app.main:app --reload

接口文档：

http://127.0.0.1:8000/docs
🔌 API 接口
创建会话
POST
/conversation

返回：

{
 "conversation_id":"xxxx"
}
AI 对话
POST
/chat

请求：

{
 "conversation_id":"xxxx",
 "question":"介绍一下 Redis"
}

返回：

text/event-stream

支持流式输出。

📈 项目亮点
基于 FastAPI 构建高性能异步 AI 服务
集成大语言模型 API，实现智能对话能力
设计 Redis + PostgreSQL 双层 Memory 架构
实现多轮上下文管理
支持 SSE 流式响应，提高用户交互体验
使用 SQLAlchemy 完成数据库 ORM 管理


🔮 后续优化方向
 RAG 知识库问答
 PDF 文档上传与解析
 Embedding 向量检索
 Chroma / Milvus 向量数据库
 用户认证系统
 Docker Compose 一键部署
 Agent 工作流
