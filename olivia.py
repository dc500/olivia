# -*- coding: utf-8 -*-

import tensorflow as tf
import json
import axon
import adapter
import checkQuestion
import brainEngine

#flags
tf.app.flags.DEFINE_boolean("terminal", False, "Run Olivia in TERMINAL mode")
tf.app.flags.DEFINE_boolean("api", False, "Run Olivia in API mode")
FLAGS = tf.app.flags.FLAGS


def oliviaTerminal():
    # chatbot main function
    ioAdapter = adapter.IOAdapter()
    classifier = adapter.Classifier()
#    checkQuestion = checkQuestion.interactiveQA()
    brain = brainEngine.QAEngines()

    while True:
        input_utterance = input("USER>> ")
        if input_utterance == "exit()":
            exit()
        else:
            utterance = ioAdapter.inputWrapper(input_utterance)
            utype = classifier.uClassifier(input_utterance)
            
            # olivia를 웹서비스화 하려면 check question 도 전체 시스템의 output 이 되도록 다시 설계해야 함
            response = brain.controller(utterance, utype)

            output_response = ioAdapter.outputWrapper(response)
            print("Olivia>> ",output_response)





def main(_):
    print("\n", "...Olivia is being developed now...", "\n")
    print("##### tensorflow version: ", tf.__version__, "#####")
    print("##### this code - Olivia - is written in python 3.6 #####")
    print("##### if you want to exit, chat \"exit()\"", "\n")
    if FLAGS.terminal:
        oliviaTerminal()
    elif FLAGS.api:
        oliviaAPI()
    else:
        print("if you want to chat with Olivia in TERMINAL, you should:")
        print("python3 olivia.py --terminal", "\n")

if __name__=="__main__":
    tf.app.run()
