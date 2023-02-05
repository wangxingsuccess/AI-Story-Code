# -*- coding: utf-8 -*-
import openai
import pyttsx3

openai.api_key = 'AI Key'

# Get the response from OpenAI API
def get_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Tell the story
def tell_story():
    # 初始化语音播报器
    engine = pyttsx3.init()

    # 设置语音播报的语言
    engine.setProperty('voice', 'zh')

    # 将文本播报为语音
    engine.say("故事天地欢迎你，小耳朵陪你一起讲故事,故事我要思考一会请小朋友耐心等待哦 么么哒")
    engine.runAndWait()
    print("故事天地欢迎你，小耳朵陪你一起讲故事")

    protagonist = input("故事名： ")
    # 启动语音播报
    engine.say("请告诉我你想听什么故事或者给故事起个名字我给你想一个")
    engine.runAndWait()
    story_prompt = f"用中文写一个500字的故事，故事名为 {protagonist}，要求故事很具有想象力、励志。"
    story = get_response(story_prompt)
    print(story+":\n")
    # 获取生成的文本
    story_text = story
    engine.say(story_text)
    # 启动语音播报
    engine.runAndWait()



tell_story()
