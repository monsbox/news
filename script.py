import os
import argparse
from notionai import NotionAI, NotionAIStream

parser = argparse.ArgumentParser()
parser.add_argument("space_id", type=str)
parser.add_argument("token", type=str)
args = parser.parse_args()
SPACE_ID = args.space_id or os.environ["SPACE_ID"]
TOKEN = args.token or os.environ["TOKEN"]


def write(prompt: str, context: str):
    ai = NotionAI(TOKEN, SPACE_ID)
    res = ai.help_me_write(prompt, context)
    print(res)


def main():
    write(
        "用中文总结下这篇文章讲了什么",
        """
          ## What motivated you to get started with Gumroad?

I love building stuff. I really enjoy the process of taking a problem and coming up with a solution, and then shipping a prototype of that solution to see how good my concept was. Most of the time, it's not that great.

But sometimes something works out really well, and then I have to decide if I actually want to work on the idea some more. Very rarely, the answer is yes. That was the case with Gumroad. The question at its core was really compelling to me: How easy could one make it to sell something?

When I first got to work, my friend, John, had started a payments company called Stripe and gave me a beta invite. That made my life a lot easier. I didn't really know what I was doing, but some of that was intentional. I don't think it’s always that advantageous to study up too much about a problem before you start working on it. Knowing too much about the space that problem occupies and its consequences can be dispiriting and might steer you away from approaching it with a clear mind. Spend a weekend being as idealistic as possible—you can always study and learn later and revisit the problem with the context and perspective of added knowledge, but you can’t do it the other way around.

A few months later, I left Pinterest to work full-time on Gumroad and raised $8MM from KPCB, Max Levchin, and other investors.
          """,
    )


if __name__ == "__main__":
    main()
