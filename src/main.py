from textnode import TextNode, TextType


def main():
    textNode = TextNode("this is a text node",
                        TextType.BOLD,
                        "https://www.boot.dev"
                        )
    print(textNode)


if __name__ == "__main__":
    main()
