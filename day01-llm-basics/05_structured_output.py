"""05 结构化输出：让模型返回可程序解析的 JSON。

模型默认吐自然语言，代码很难直接用。用 JSON Mode（或 Function Calling）拿到结构化结果，
Agent 才能把模型输出接进代码逻辑——这正是后面 Function Calling 章节的铺垫。
运行：python3 05_structured_output.py --mock
"""
import json

from llm_client import get_client


def main():
    client, is_mock = get_client()
    print(f"（模式：{'离线 Mock' if is_mock else '真实调用'}）\n")

    messages = [{
        "role": "user",
        "content": (
            "提取下面这句话的实体，只返回 JSON：{\"name\":,\"type\":,\"feature\":}。"
            "句子：通义千问是阿里发布的对话大模型。"
        ),
    }]

    if is_mock:
        content = '{"name": "通义千问", "type": "对话大模型", "feature": "阿里发布"}'
        print("模型返回：", content)
    else:
        resp = client.create(messages=messages, temperature=0, response_format={"type": "json_object"})
        content = resp.choices[0].message.content
        print("模型返回：", content)

    data = json.loads(content)
    print("解析为对象：", data)
    print(
        "提示：真实项目里用 JSON Mode / Function Calling 拿到结构化结果，"
        "Agent 才能把模型输出接进代码逻辑（这正是后面 Function Calling 的铺垫）。"
    )


if __name__ == "__main__":
    main()
