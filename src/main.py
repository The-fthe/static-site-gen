from textnode import TextNode
from enum import Enum


def main():
    # textNode = Enum('TextNode', {
    #                 'TEXT': "this is a text node", 'TEXT_TYPE': "bold", 'URL': "https://www.boot.dev"})
    textNode = TextNode("this is a text node", "bold",  "https://www.boot.dev")
    print(textNode)


if __name__ == "__main__":
    main()
