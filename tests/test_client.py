from ica_eval import client


class FakeResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return {"message": {"content": "ok"}}


def test_chat_asks_for_deterministic_output(monkeypatch):
    sent = {}

    def fake_post(url, json, timeout):
        sent.update(url=url, json=json)
        return FakeResponse()

    monkeypatch.setattr(client.requests, "post", fake_post)

    reply = client.chat("llama3.1:8b", [{"role": "user", "content": "hi"}])

    assert reply == "ok"
    assert sent["url"].endswith("/api/chat")
    assert sent["json"]["options"] == {"temperature": 0, "seed": 42}
    assert sent["json"]["stream"] is False
