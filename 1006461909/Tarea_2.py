{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00001-34c40f61-06ce-4418-bbce-e2ce90ce485d",
        "deepnote_cell_type": "markdown",
        "id": "QC4VVNb6F_yr"
      },
      "source": [
        "<div style=\"float: right;\" markdown=\"1\">\n",
        "    <img src=\"https://www.python.org/static/community_logos/python-logo-master-v3-TM.png\">\n",
        "</div>\n",
        "\n",
        "PYTHON\n",
        "==\n",
        "<a href=\"https://colab.research.google.com/github/restrepo/ComputationalMethods/blob/master/material/overview-python.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>\n",
        "\n",
        "Python is an interpreted programming language oriented to easy-readable coding, unlike compiled languages like C/C++ and Fortran, where the syntax usually does not favor the readability. This feature makes Python very interesting when we want to focus on something different than the program structure itself, e.g. on Computational Methods, thereby allowing to optimize our time, to debug syntax errors easily, etc.\n",
        "\n",
        "\n",
        "[Official page](https://www.python.org/)\n",
        "\n",
        "[Wikipedia](http://en.wikipedia.org/wiki/Python)\n",
        "\n",
        "Python Philosophy\n",
        "--\n",
        "1. Beautiful is better than ugly.\n",
        "2. Explicit is better than implicit.\n",
        "3. Simple is better than complex.\n",
        "4. Complex is better than complicated.\n",
        "5. Flat is better than nested.\n",
        "6. Sparse is better than dense.\n",
        "7. Readability counts.\n",
        "8. Special cases aren't special enough to break the rules. (Although practicality beats purity)\n",
        "9. Errors should never pass silently. (Unless explicitly silenced)\n",
        "10. In the face of ambiguity, refuse the temptation to guess.\n",
        "11. There should be one-- and preferably only one --obvious way to do it. (Although that way may not be obvious at first unless you're Dutch)\n",
        "12. Now is better than never. (Although never is often better than right now)\n",
        "13. If the implementation is hard to explain, it's a bad idea.\n",
        "14. If the implementation is easy to explain, it may be a good idea.\n",
        "15. NameSpaces are one honking great idea -- let's do more of those!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00002-31d14584-489a-45c7-91b3-23805b9a7676",
        "deepnote_cell_type": "markdown",
        "id": "PsvrRJSXF_yt"
      },
      "source": [
        "- - - "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00003-0e2a09eb-5786-4a95-8200-d83226d3ffb8",
        "deepnote_cell_type": "markdown",
        "id": "rnVM9axRF_yu"
      },
      "source": [
        "- [String, Integer, Float](#String,-Integer,-Float)\n",
        "- [Functions I](#Functions-I) \n",
        "- [Hello World!](#Hello-World!) \n",
        "- [Arithmetics](#Arithmetics)\n",
        "- [Lists, Tuples and Dictionaries](#Lists,-Tuples-and-Dictionaries)\n",
        "- [Bucles and Conditionals](#Bucles-and-Conditionals)\n",
        "- [Functions II](#Functions-II)\n",
        "\n",
        "## Biblography\n",
        "[1f] Ani Adhikari and John DeNero, [Computational and Inferential Thinking](https://www.inferentialthinking.com/chapters/intro.html)<br/>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00004-81e7146e-c6ee-4365-bf24-e91f88b7ecf8",
        "deepnote_cell_type": "markdown",
        "id": "ru2dYuqiF_yu"
      },
      "source": [
        "- - - "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00005-13c84412-9812-4fbe-91e9-226f0e561b93",
        "deepnote_cell_type": "markdown",
        "id": "hbVuNve0Lp_-"
      },
      "source": [
        "# String, Integer, Float\n",
        "The basic types of variables in Python are:\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00006-65a6724f-f322-49ed-9e09-6bcbf9457264",
        "deepnote_cell_type": "markdown",
        "id": "oO8rcC_aMYXO"
      },
      "source": [
        "`str`:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00007-e253803b-ed4b-4907-9356-4a83b0039b30",
        "deepnote_cell_type": "markdown",
        "id": "POJ9rA7A40WK",
        "tags": [
          "popout"
        ]
      },
      "source": [
        "Illustrated with the `hello world` standard"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00008-91be0a32-abda-4520-a914-714ff10afa93",
        "deepnote_cell_type": "code",
        "id": "5_KEVfViMOZC"
      },
      "outputs": [],
      "source": [
        "#Strings\n",
        "hello='hola'"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00009-969a988b-eb14-46a7-816d-4e848b57ed69",
        "deepnote_cell_type": "markdown",
        "id": "n6ff3fKrMdHF"
      },
      "source": [
        "`int`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "cell_id": "00010-c92b506d-2fe8-417d-bb15-d35301b5e4b3",
        "deepnote_cell_type": "code",
        "id": "Bm-RxdlxMVGU"
      },
      "outputs": [],
      "source": [
        "#Integer\n",
        "n=3"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00011-2853f608-5fe9-4ee1-81b5-22c17a614390",
        "deepnote_cell_type": "markdown",
        "id": "P6JSYRm_Mh41"
      },
      "source": [
        "`float`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00012-bb0745de-12de-47dc-9a3b-3019d0034d3f",
        "deepnote_cell_type": "code",
        "id": "XJF1vwxJMlyl"
      },
      "outputs": [],
      "source": [
        "x=3.5"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00013-41c6f7d2-9e69-4116-9779-197608446a46",
        "deepnote_cell_type": "markdown",
        "id": "wTzMkndjJFZp"
      },
      "source": [
        "# Functions I\n",
        "Python includes a battery of predefined functions which takes an input and generates an output. For example, to check the type of variable we can used the\n",
        "predefined function\n",
        "## `isinistance`:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00014-d3d484c8-fe92-4249-823b-33b8cfb50f67",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "id": "4K96FCuENYCd",
        "outputId": "2da1940e-179b-4722-c6a2-cdd8e210686c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 5,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "isinstance(hello,str)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00015-51d87b6c-cae5-4fe5-adac-13c50bea1679",
        "deepnote_cell_type": "markdown",
        "id": "YeFccBUZNggD"
      },
      "source": [
        "**Activity**: In the next cell check if `n`  is a `float` type of variable"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "cell_id": "00016-72e793a7-fa96-46d6-b80d-6cb00842b564",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "deepnote_cell_type": "code",
        "id": "x3mFZU1aNu-U",
        "outputId": "2b216250-52fe-4ed1-b3fb-b078ba986249"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ],
      "source": [
        "isinstance(n, float)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00017-787585d6-0d9d-4993-9a1e-77f716393cc8",
        "deepnote_cell_type": "markdown",
        "id": "RQJLzZTxNxGb"
      },
      "source": [
        "## `print`"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00018-12f271e5-3695-44c1-8ddb-3dcf95f8c75d",
        "deepnote_cell_type": "markdown",
        "id": "N7GTR9AiM5Xm"
      },
      "source": [
        "See: https://pyformat.info/\n",
        "\n",
        "To write the _Hello world_ program in python we must first introduce the concept of function. It is the same in mathematics, were something called function receives a number and return back another number. For example, the function to square a number is\n",
        "\\begin{equation}\n",
        "f(x)=x^2\\,,\n",
        "\\end{equation}\n",
        "$x$ is called the argument of the function $f$, and the _returned_ value is the evaluation of $f(x)$.\n",
        "\n",
        "In `Python` there are a lot of such a functions.\n",
        "In particular there is a function called `print` which takes strings (see below) as input and return the same string as output. In this way, the __hello world__ program in Python is one of the most simple between all the programming languages:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00019-517c05f6-21d9-426a-a296-d9dde08cab22",
        "deepnote_cell_type": "markdown",
        "id": "PJOXAlbAF_yv"
      },
      "source": [
        "# Hello World!"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00020-16a2021c-4785-4ccb-863f-7df6efc8aeae",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "Cmd-Wx7oF_yw",
        "outputId": "923773c2-46e1-4f85-9728-30d47dbeff41"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Hello World!\n"
          ]
        }
      ],
      "source": [
        "print('Hello World!')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00021-28b16aec-3e64-4af4-84d5-78267d544c8c",
        "deepnote_cell_type": "markdown",
        "id": "_WerUXfIF_y0"
      },
      "source": [
        "And also allows scripting: *(This code should be copied on a file 'hello.py')*"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00022-a1283afa-00ff-4c65-9fad-59500a590fd6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "WTvsRsI_F_y1",
        "outputId": "37adc2e2-26a0-4e88-fea4-f7289cc8f9b3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Hello World!\n"
          ]
        }
      ],
      "source": [
        "#! /usr/bin/python\n",
        "\n",
        "#This is a comment\n",
        "print('Hello World!')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00023-13a8d280-1ab3-4b2d-b467-abcbaafbc948",
        "deepnote_cell_type": "markdown",
        "id": "cvkfIERrN6GT"
      },
      "source": [
        "The recommended way to print a variable in Python is to use the `.format` _method_ of the function `print` by preceding the sring with the letter `f`. Inside the string any variable between curly brackets, `{variable}`, can be used"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00024-811d5082-ffdd-42f4-92fd-53ae42eb27da",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 10,
        "execution_start": 1626453090430,
        "id": "4iiFnX3GOSix",
        "outputId": "189ad787-6654-4205-b084-9b3286a1793f",
        "source_hash": "3e036be2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Hello World!\n"
          ]
        }
      ],
      "source": [
        "hello='Hello World!'\n",
        "print(f'{hello}')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00025-1bac035d-fc1f-4347-a35b-7ed20fd9e7da",
        "deepnote_cell_type": "markdown",
        "id": "mAOFOHQtOlYD"
      },
      "source": [
        "__Activity__: Change the values of the previous string variables to print `Hello World!` in Spanish "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Wd1e8WjtXafZ",
        "outputId": "2b66dee9-d53b-4780-f5d1-2f73639d7216"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hola mundo!\n"
          ]
        }
      ],
      "source": [
        "hello='hola mundo!'\n",
        "print(f'{hello}')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qqkIo_dJXafZ",
        "outputId": "3ebad531-8d7d-4e92-8b39-6d4c7bcdf488"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "23456.57\n"
          ]
        }
      ],
      "source": [
        "x=23456.5678545\n",
        "print(f'{x:.2f}')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hh3gAo5HXafZ"
      },
      "source": [
        "__Activity__: Print with 3 decimal places"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8eo8kRdMXafa",
        "outputId": "6c41e9da-bdd2-439b-a0f9-d38828b4a50d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "12345.137\n"
          ]
        }
      ],
      "source": [
        "x = 12345.13654367\n",
        "print(f'{x:.3f}')"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "cell_id": "00026-4805810c-5c15-4710-8026-bae638fb8f8c",
        "deepnote_cell_type": "markdown",
        "id": "lckGJ4UsPBSR"
      },
      "source": [
        "# Functions"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00027-592d06b0-4e0f-433a-bdeb-a29ddc6ac39d",
        "deepnote_cell_type": "markdown",
        "id": "KJTsJ2exKcSQ"
      },
      "source": [
        "In `Python` it is possible also to create new [functions](https://en.wikibooks.org/wiki/Python_Programming/Functions). We illustrate the format to define a function in `Python` with the implementation of the function $f(x)=x^2$, where to write an exponent: ${}^2$, in Python we must use the format: `**2`."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00028-7b74f015-b720-4b86-b279-41314b94db49",
        "deepnote_cell_type": "markdown",
        "id": "ADy7KEsUXafa"
      },
      "source": [
        "## Implicit functions"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00029-d7d95097-f42c-415b-a1bd-9c7704717b9d",
        "deepnote_cell_type": "code",
        "id": "SLI_RmTIKr_2"
      },
      "outputs": [],
      "source": [
        "f=lambda x:x**2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00030-26b39a17-b613-4fc8-94f0-5e6c89e2f50d",
        "deepnote_cell_type": "code",
        "id": "l9Zrtp3XXafa",
        "outputId": "1f55f21e-b71b-4f6c-dd6e-2607ef8d64c6"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 16,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "isinstance(f,str)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00031-79297844-077e-4635-8e17-58b38e1e0ce2",
        "deepnote_cell_type": "code",
        "id": "wZ2U0_OsXafb",
        "outputId": "c9a44e06-d002-4203-a206-0582fd386b4e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "function"
            ]
          },
          "execution_count": 17,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "type(f)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00032-98229684-c9cb-4db0-8998-ca3a47b7de9d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "kSBRdi67dfD1",
        "outputId": "25c8f546-806d-4462-d87a-f8cc63c5d536"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "9"
            ]
          },
          "execution_count": 19,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "f(3)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00033-61dd30ec-2a6d-4012-b387-d080d1fd8989",
        "deepnote_cell_type": "markdown",
        "id": "R3j70bwqF_1Y"
      },
      "source": [
        "## Explicit functions"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00034-fb1ab9ee-21c4-4421-8b9b-5c48a4c8b7e2",
        "deepnote_cell_type": "markdown",
        "id": "rDbINWXVXafb"
      },
      "source": [
        "The standard function build may include the help for the function"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00035-e180aab0-ab38-489f-ba08-34be6332faa2",
        "deepnote_cell_type": "code",
        "id": "XUwDF67gXafc"
      },
      "outputs": [],
      "source": [
        "def f(x):\n",
        "    '''\n",
        "    Calculates the square of `x`\n",
        "    '''\n",
        "    return x**2"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00036-c65adff0-6b70-4d2c-a011-8fca30c55934",
        "deepnote_cell_type": "markdown",
        "id": "xBHsimi0Xafc"
      },
      "source": [
        "f(5)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00037-38b7a17c-cd1d-48fe-b1ea-5a5072610698",
        "deepnote_cell_type": "code",
        "id": "8TGfhY8LXafc",
        "outputId": "3dcf06e7-d358-41ad-ce6b-ca9f11ed9393"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Help on function f in module __main__:\n",
            "\n",
            "f(x)\n",
            "    Calculates the square of `x`\n",
            "\n"
          ]
        }
      ],
      "source": [
        "help(f)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00038-462d3558-b374-4618-bd59-a80b2d0b111c",
        "deepnote_cell_type": "markdown",
        "id": "DJwBYqi440XD"
      },
      "source": [
        "The full list of built-in functions is in https://docs.python.org/3/library/functions.html and the specific help for a function, for example `print` can be checked with https://docs.python.org/3/library/functions.html#print"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00039-22606d64-26bf-44cb-8348-1d4b575937b5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "z3IAaPwJF_1Z",
        "outputId": "f550c7a2-861b-4c92-e5ac-f816531e2b54"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "6"
            ]
          },
          "execution_count": 129,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "def f(x,y):\n",
        "    '''\n",
        "    Multiply two numbers\n",
        "    '''\n",
        "    return x*y\n",
        "f(3,2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00040-961f1860-4b88-4d6f-9e2c-dfadf8d90088",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "hMkLVbRRF_1a",
        "outputId": "1fe169d5-b147-448d-89ba-63063ef02d92"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "6"
            ]
          },
          "execution_count": 130,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#It is possible to assign default arguments\n",
        "def f(x,y=2):\n",
        "    '''\n",
        "    Multiply two numbers. By default the second is 2\n",
        "    '''    \n",
        "    return x*y\n",
        "#When evaluating, we can omit the default argument\n",
        "f(3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00041-1fd18671-3f9e-4952-9858-17084a1d1a7e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "Ee_8WkNdnnaj",
        "outputId": "4a6511b0-42aa-467c-92a4-b02765b3f741"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "6"
            ]
          },
          "execution_count": 131,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "f(2,3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00042-61782059-8e73-432a-8637-7ac4f91820d2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "uCLluCGVnqWj",
        "outputId": "a43bcd34-b8ee-4279-889d-d92ee71618ac"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "10"
            ]
          },
          "execution_count": 132,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "f(2,y=5)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00043-0d8d6730-9581-4ed8-b5b9-ee99fe9e7713",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "deepnote_cell_type": "code",
        "id": "Eh6jou-TF_1c",
        "outputId": "d82b0602-72f2-4e18-9260-78a71ebca88c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "f(1,2)= 1\n",
            "f(2,1)= 2\n"
          ]
        }
      ],
      "source": [
        "#It is possible to specify explicitly the order of the arguments\n",
        "def f(x,y):\n",
        "    '''\n",
        "    evaluates x to the power y\n",
        "    '''    \n",
        "    return x**y\n",
        "print( 'f(1,2)=',f(1,2) )\n",
        "print( 'f(2,1)=',f(y=1,x=2) )"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00044-b18eb58e-48c1-4974-834a-5360ab115abc",
        "deepnote_cell_type": "markdown",
        "id": "PYyDcKZ5F_1e"
      },
      "source": [
        "## Implicit functions of several arguments"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00045-b10fb053-57c3-4fba-be8d-f163bf0cf2a9",
        "deepnote_cell_type": "markdown",
        "id": "-suvy_mEF_1e"
      },
      "source": [
        "Implicit functions are usdeful when we want to use a function once."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00046-76cd6d35-3e2b-47a0-9edb-5f9a8dc2cb2e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "FMTOmWFYF_1f",
        "outputId": "8e7c1b41-a48e-4a9b-bd3c-4f4a9fd9cf78"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "9"
            ]
          },
          "execution_count": 138,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "f = lambda x,y: x**y\n",
        "f(3,2)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MBVufvgDXafe"
      },
      "source": [
        "## Nested functions"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00047-126140fa-fc08-4d74-874a-d90d37dd86da",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 70
        },
        "deepnote_cell_type": "code",
        "id": "mWGO2OHrF_1g",
        "outputId": "4532bcfe-9ffc-49cc-bdd2-d3077580246f"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "4\n",
            "16\n",
            "Implicit: f(2)^2 = 16\n"
          ]
        }
      ],
      "source": [
        "#It is possible to pass functions as arguments of other function\n",
        "def f2( f, x ):\n",
        "    return f(x)**2\n",
        "\n",
        "#We can define a new function explicitly\n",
        "def f(x):\n",
        "    return x+2\n",
        "\n",
        "print(f(2))\n",
        "print(f2(f,2))\n",
        "\n",
        "\n",
        "#Or define the function implicitly\n",
        "print (\"Implicit: f(2)^2 =\", f2(lambda x:x+2,2) )"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fgftD3-sXaff"
      },
      "source": [
        "## Inner functions with returned internal function"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00048-66af3fe0-dd06-4063-aece-2a26de1531db",
        "deepnote_cell_type": "code",
        "id": "sKPY7uoHXaff"
      },
      "outputs": [],
      "source": [
        "def hola(func):\n",
        "    def function_wrapper(x):\n",
        "        res = 'hola mundo '+str(func(x))\n",
        "        return res\n",
        "    return function_wrapper\n",
        "\n",
        "def mundo(n):\n",
        "    return n+' y despiadado'"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NRQn_vzeXaff",
        "outputId": "e1251947-5791-4b31-bbfa-f4b5202cc168"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "'hola mundo cruel y despiadado'"
            ]
          },
          "execution_count": 18,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "foo=hola(mundo)\n",
        "foo('cruel')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0eWc7-r_Xaff"
      },
      "source": [
        "or just"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "levfzwKFXaff",
        "outputId": "f07d8aa7-e53a-488a-dcb7-238d6bb5c00c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "'hola mundo cruel y despiadado'"
            ]
          },
          "execution_count": 19,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "hola(mundo)('cruel')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SWkjACbqXafg"
      },
      "source": [
        "## Decorators\n",
        "From: [[@]](https://realpython.com/primer-on-python-decorators/) https://realpython.com/primer-on-python-decorators/\n",
        "> By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.\n",
        "\n",
        "See also: https://www.python-course.eu/python3_decorators.php.\n",
        "\n",
        "The previos function `hola` can be used as a decorator, in a such way that it is not necesary to call it directly but only to call its argument"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "d2lKhmklXafg"
      },
      "outputs": [],
      "source": [
        "@hola\n",
        "def mundano(n):\n",
        "    return n+' y despiadado'\n",
        "\n",
        "@hola\n",
        "def mundito(n):\n",
        "    return n+' y floreciente'"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tnS0LwQdXafg"
      },
      "source": [
        "Instead `of hola(mundano)('cruel')` we can just use directly the new decorated function:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "EIByN3jsXafg"
      },
      "outputs": [],
      "source": [
        "mundano('cruel')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vb0ESEfAXafh"
      },
      "outputs": [],
      "source": [
        "mundito('brillante')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EiudC44DXafh"
      },
      "source": [
        "[[@]](https://realpython.com/primer-on-python-decorators/):\n",
        "> Put simply: __decorators wrap a function, modifying its behavior.__"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00049-e128fdf5-6d40-4e6d-a8a2-25bd944de81c",
        "deepnote_cell_type": "markdown",
        "id": "tmc45kxUF_y4"
      },
      "source": [
        "# Arithmetics"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00050-56a76643-a756-4bd2-946f-8dbd126ebf74",
        "deepnote_cell_type": "markdown",
        "id": "ozwFot0rF_y4"
      },
      "source": [
        "## Sum"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00051-74b45186-581d-46f3-be38-38b781b27e99",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "URMyrhmqF_y5",
        "outputId": "6b38d80c-b3a3-481d-f835-94d65ac766b5"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "10.78"
            ]
          },
          "execution_count": 26,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "5.89+4.89"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00052-7b94f9d9-d4e1-4a12-a5b9-14142d764d39",
        "deepnote_cell_type": "markdown",
        "id": "0DNu3gWKdwIy"
      },
      "source": [
        "**Activity**: Sum strings:\n",
        "Hint: use `+' '+`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "cell_id": "00053-04becf08-bc65-42cb-b09f-5d7896e58c9a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "deepnote_cell_type": "code",
        "id": "68e7G-PRd86Q",
        "outputId": "1df91557-55a9-430b-9152-a2b170da5420"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "11.3"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ],
      "source": [
        "4.28+7.02"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00054-6e9b2fb1-ad02-44da-a1fc-78acf7f739ee",
        "deepnote_cell_type": "markdown",
        "id": "1dE0l0jyd9wJ"
      },
      "source": [
        "**Activity**: Sum integers"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00055-358e4396-8a80-47d3-ac09-2f7596fd02ed",
        "deepnote_cell_type": "code",
        "id": "TAYYWZwveGfR",
        "outputId": "a39c415b-f8a1-4bc5-c5f6-791ae43d5d44"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "5"
            ]
          },
          "execution_count": 33,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "2+3"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00056-229969a9-1a88-4bfa-94eb-0315f479314a",
        "deepnote_cell_type": "markdown",
        "id": "AK5CSon3PDnW"
      },
      "source": [
        "**Example**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00057-9868f3b3-c5f8-41b4-a512-2cb6379346f5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "id": "WI8fn1qdeWvG",
        "outputId": "76fbecd4-37b0-4960-e6d8-7bf33fe03bf6"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Hola Mundo!\n"
          ]
        }
      ],
      "source": [
        "print(hello+' '+world+'!')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00058-51897368-a994-44cc-bbac-d59edcaf405d",
        "deepnote_cell_type": "markdown",
        "id": "-fCXEiSsF_y8"
      },
      "source": [
        "## Multiplication"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00059-9fb7b1b4-9f96-40f2-b98b-70e101a3eb5c",
        "deepnote_cell_type": "code",
        "id": "vu7SzdLjF_y9",
        "outputId": "563be8e8-08b2-4f5f-92a3-4bc0842e3bb7"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "540.0"
            ]
          },
          "execution_count": 35,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "120*4.5"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00060-da533ec0-10e7-4d04-ba30-cf5e014fe793",
        "deepnote_cell_type": "markdown",
        "id": "wC3Jfp4tPR2a"
      },
      "source": [
        "**Example** String multiplied by integer:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00061-c262fd98-8a47-4c8a-85bd-583b5c2ffba5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "U6X_16Bpelup",
        "outputId": "f8017363-25b2-49c9-e222-1821da24ef29"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "================================================================================\n"
          ]
        }
      ],
      "source": [
        "print('='*80)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00062-85e7cd59-82e0-4a8f-927e-8c4de20890bf",
        "deepnote_cell_type": "markdown",
        "id": "jtskAuqQF_zA"
      },
      "source": [
        "## **Division**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00063-eaf6081c-d23e-41a3-b7b0-9b9fc661fa2c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "id": "QsCpsAd8F_zA",
        "outputId": "7dded816-e2c9-4862-ba72-bec93846fc8c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "33.333333333333336"
            ]
          },
          "execution_count": 37,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Python 3 does support complete division\n",
        "100/3"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00064-04572ec2-eccf-49da-b738-3d5dfb1a641f",
        "deepnote_cell_type": "code",
        "id": "_4K2vuGqF_zD",
        "outputId": "e2a3e187-4bea-4580-dd2d-1a8819bd4614"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "33.333333333333336"
            ]
          },
          "execution_count": 38,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "100/3."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00065-b9748840-0fa4-4767-ae5f-9ae17ffd2ceb",
        "deepnote_cell_type": "markdown",
        "id": "Svm9I6uvXafk"
      },
      "source": [
        "Force integer division"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00066-418e827f-e17d-475a-ad48-8c1f159c63cf",
        "deepnote_cell_type": "code",
        "id": "qWVqiGU6Xafk",
        "outputId": "2f349bba-56f6-4346-faa0-4f0bb026c129"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "33"
            ]
          },
          "execution_count": 39,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "100//3"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00067-a2553e7c-3180-49bd-ae9d-b91598376b9b",
        "deepnote_cell_type": "markdown",
        "id": "x7xHh9tjF_zJ"
      },
      "source": [
        "## **Module**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00068-739595f2-6f11-4c01-8325-7937294b615f",
        "deepnote_cell_type": "code",
        "id": "R4a7H6dmF_zJ",
        "outputId": "4fa12d47-806a-4b49-b521-32ec36986b4a"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "execution_count": 8,
          "metadata": {
            "tags": []
          },
          "output_type": "execute_result"
        }
      ],
      "source": [
        "10%2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00069-8542809a-a3a8-4011-976f-cba20d0c8d2c",
        "deepnote_cell_type": "code",
        "id": "Z9ST9W04F_zM",
        "outputId": "6fe779e1-46b9-4621-d99f-e570706c237b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "execution_count": 9,
          "metadata": {
            "tags": []
          },
          "output_type": "execute_result"
        }
      ],
      "source": [
        "20%3"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00070-8ad8abec-b278-45e3-b3a4-aafc43b797cf",
        "deepnote_cell_type": "markdown",
        "id": "2iWjCW7tF_zF"
      },
      "source": [
        "## **Power**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00071-67f91ae1-5f80-47a8-9283-001b5c4ea750",
        "deepnote_cell_type": "code",
        "id": "ShgiDMOaF_zG",
        "outputId": "8b2f08a8-c273-4e61-b81b-53dbbe0402fb"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "64"
            ]
          },
          "execution_count": 42,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "2**6"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00072-40ada915-f658-4795-8cdb-481dc6f2b7d7",
        "deepnote_cell_type": "markdown",
        "id": "8_EWbqIzF_zQ"
      },
      "source": [
        "## **Scientific notation**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00073-6fb987c1-e3be-48c1-aa88-8642ff00bf3c",
        "deepnote_cell_type": "markdown",
        "id": "2eMbujkrXafl"
      },
      "source": [
        "$1\\times 10^3=10^3=1000$"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00074-3150bb4a-fa4a-44b5-8950-948a88aed8a5",
        "deepnote_cell_type": "code",
        "id": "LnQFXIGOXafl",
        "outputId": "8181707f-c445-4d23-f549-45fbee666b0c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "1000.0"
            ]
          },
          "execution_count": 44,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "1E3"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00075-004b6451-067c-4c99-8a72-c0dcd2f58abe",
        "deepnote_cell_type": "markdown",
        "id": "yaNVgFJRXafm"
      },
      "source": [
        "$2\\times 10^3=2000$"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00076-fcd6409c-7f6f-401c-8956-e8c1d42b9344",
        "deepnote_cell_type": "code",
        "id": "MzI0MRX3Xafm",
        "outputId": "c88b839e-2d47-4a93-aabc-1037858f6c67"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "2000.0"
            ]
          },
          "execution_count": 46,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "2E3"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00077-75a926f3-b216-4e39-9895-8b62d2e07a49",
        "deepnote_cell_type": "markdown",
        "id": "aSr2SlYnXafm"
      },
      "source": [
        "$$\\frac{ \\dfrac{10^{24}}{3}+2.9\\times 10^{23}}{10^2}$$"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00078-3b709032-f2e1-4d3d-b08e-2458850c2ab2",
        "deepnote_cell_type": "code",
        "id": "1rf2SYTRF_zR",
        "outputId": "3054b29a-fa77-4e7e-c0ca-584f52f55ea5"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "6.233333333333333e+25"
            ]
          },
          "execution_count": 47,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "(1.0e24/3. + 2.9e23)/1e-2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00079-829fc58e-d927-4e10-9ffe-acca3f536cbc",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 4,
        "execution_start": 1626454198013,
        "id": "K0H39NBm40Xz",
        "source_hash": "1abb969e"
      },
      "outputs": [],
      "source": [
        "sin=0.3"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00080-29f9ddf2-f106-4b9e-af07-9a32efcbb972",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 15,
        "execution_start": 1626454198619,
        "source_hash": "662fdaec",
        "tags": [],
        "id": "9zEU0yCYXafn",
        "outputId": "9334c223-b8ab-4098-adfd-8b2a6a39d39c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 4,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "isinstance(sin,float)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00080-cc0e2648-3bac-448d-befc-5f0a4e900a88",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 1,
        "execution_start": 1626454747098,
        "id": "vWOkR85240X2",
        "source_hash": "b00e867f"
      },
      "outputs": [],
      "source": [
        "from math import *"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00082-99e102f2-5b26-479a-8cfc-0c7346f024b5",
        "deepnote_cell_type": "markdown",
        "id": "7K7srcsoXafn"
      },
      "source": [
        "Keep the name space"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00083-70b46540-3ac9-4cf3-8270-e51d30c34423",
        "deepnote_cell_type": "markdown",
        "id": "-qzUFvylXafn"
      },
      "source": [
        "Use `name.last_name`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00084-39000ce2-90d5-4536-969e-cb0a66d97e85",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 13,
        "execution_start": 1626454762697,
        "source_hash": "662fdaec",
        "id": "kzdEPPygXafn",
        "outputId": "487503bb-b7b3-4d31-9487-ec5951ce09c2"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 9,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "isinstance(sin,float)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00085-40c2fbb5-7a0e-4fac-b422-98b2d7bef868",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 15,
        "execution_start": 1626454752505,
        "source_hash": "2ceac8dc",
        "tags": [],
        "id": "Gl3KHYzqXafo",
        "outputId": "658f416d-0693-4ca9-aeb9-2a6dfa72ad1e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<function math.sin(x, /)>"
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "sin"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00085-4dd1c9e8-27bb-46c8-a193-9febc40c815b",
        "deepnote_cell_type": "code",
        "id": "yfYz0zLKNqA4"
      },
      "outputs": [],
      "source": [
        "import math as m\n",
        "import cmath as cm\n",
        "import numpy as np\n",
        "#Recommended option:\n",
        "import numpy.lib.scimath as sc"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00086-66781195-0577-4bcd-9717-cbbd5ef49e12",
        "deepnote_cell_type": "code",
        "id": "65ipUbb2Xafo",
        "outputId": "c0686107-522f-4276-9392-27da7a29d437"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 54,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "isinstance(sin,float)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00087-1507b2ca-4e3a-40b9-851f-370969c6ebcd",
        "deepnote_cell_type": "code",
        "id": "HajlqR82Xafp",
        "outputId": "8e5ae637-ef79-4940-8b25-4e7782d077cb"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0.479425538604203"
            ]
          },
          "execution_count": 55,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "m.sin(0.5)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00088-01566e4d-82a9-4db8-8efa-40b4829006bb",
        "deepnote_cell_type": "code",
        "id": "bS342cFhXafp",
        "outputId": "12c22a1d-e436-4010-96ee-99e1a6e62e2b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(0.479425538604203+0j)"
            ]
          },
          "execution_count": 56,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "cm.sin(0.5)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00089-859202c9-64eb-46c0-983f-a87880c0fb3c",
        "deepnote_cell_type": "code",
        "id": "ZmLUZhxfXafp",
        "outputId": "8fca2873-42b6-4cba-bf16-da6f12c40965"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0.479425538604203"
            ]
          },
          "execution_count": 57,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "np.sin(0.5)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00090-c84c0fbe-64ce-4eab-8c36-e31213a5207b",
        "deepnote_cell_type": "code",
        "id": "X4pWyhTkXafp",
        "outputId": "661b9ccf-a922-435d-8e18-0dbe92d9dc2f"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/home/restrepo/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:1: DeprecationWarning: scipy.sin is deprecated and will be removed in SciPy 2.0.0, use numpy.sin instead\n",
            "  \"\"\"Entry point for launching an IPython kernel.\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "0.479425538604203"
            ]
          },
          "execution_count": 58,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "sp.sin(0.5)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00091-d49ebd94-56ff-4f1f-a968-52e4efe9dad3",
        "deepnote_cell_type": "markdown",
        "id": "rf3I0p_lnix5"
      },
      "source": [
        "## Complex numbers"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00092-b3263a70-7d32-4852-a5d6-7877f102554d",
        "deepnote_cell_type": "code",
        "id": "fmM9qkUWXafq",
        "outputId": "2e4401b2-7943-4445-d103-0ba3a5e987ee"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(-1+0j)"
            ]
          },
          "execution_count": 1,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "1j**2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00093-1a722771-b290-4e56-9e93-97420e2432e6",
        "deepnote_cell_type": "code",
        "id": "FV8LAGKJNqA7"
      },
      "outputs": [],
      "source": [
        "z=2+3.2j"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00094-3d02d79e-c217-43fd-a8f4-c03e9b6d89b7",
        "deepnote_cell_type": "code",
        "id": "pNOydNUO40YE",
        "outputId": "ea96f74f-c1db-46ff-cb2d-85cf35b533ba"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 4,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "isinstance(z,complex)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00095-f5a5c7b6-4ad5-49c8-b8d4-730479bec16e",
        "deepnote_cell_type": "markdown",
        "id": "y9HbGaRenix8"
      },
      "source": [
        "Attributes and methods:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00096-07b4ca2c-9701-4486-8424-bd8ec52a8c20",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "5nHDx7wLNqA9",
        "outputId": "b0dded95-9e31-4a4c-e72e-d307a5aa8302"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(2.0, 3.2, (2-3.2j))"
            ]
          },
          "execution_count": 4,
          "metadata": {
            "tags": []
          },
          "output_type": "execute_result"
        }
      ],
      "source": [
        "z.real,z.imag,z.conjugate()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00097-d50da332-4aec-4410-a0db-cf58ae5caf27",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "WVfLo4mINqBA",
        "outputId": "a45257c5-f1f6-4ca8-b32d-0e2f3c30bcf6"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(8+12.8j)"
            ]
          },
          "execution_count": 6,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "z+3*z"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00098-58b18cb4-21e6-48f4-9086-6fb8795770fa",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "cDLf56VpNqBE",
        "outputId": "5b55beba-bf25-4a21-c30e-52079fece0c1"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(-6.240000000000002+12.8j)"
            ]
          },
          "execution_count": 7,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "z*z"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00099-07cadcdf-0781-4f96-9efa-3c753e2fd6d5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "TAZa5L1RNqBG",
        "outputId": "263ad031-f5f7-418c-8e54-2f2f2f85c45e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(14.240000000000002+0j)"
            ]
          },
          "execution_count": 9,
          "metadata": {
            "tags": []
          },
          "output_type": "execute_result"
        }
      ],
      "source": [
        "z*z.conjugate()"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "cell_id": "00100-faa6110d-55de-40a1-86c8-56ce8aa5aa9d",
        "deepnote_cell_type": "markdown",
        "id": "nK4EI5bH40YX"
      },
      "source": [
        "`math` does not work with complex numbers"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00101-c9775239-ca6d-42ab-b7fa-7f9189334d40",
        "deepnote_cell_type": "code",
        "id": "sPxDr2BSNqBK"
      },
      "outputs": [],
      "source": [
        "m.asin(2+0j)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00102-cbbdaece-e706-4de6-98bd-8f43d8d35739",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "tb5p6SxcNqBO",
        "outputId": "e403c20a-6804-4742-f39a-aa4b69e8a6bf"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(1.5707963267948966+1.3169578969248166j)"
            ]
          },
          "execution_count": 163,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "cm.asin(2)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00103-746e65d9-8d08-4878-b80f-087e11660d00",
        "deepnote_cell_type": "markdown",
        "id": "sumSAgIRXafs"
      },
      "source": [
        "`numpy` requires proper input"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00104-7d842a7e-551f-4b86-8cda-aaf9002436d9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 88
        },
        "deepnote_cell_type": "code",
        "id": "CrFG7Wkko2ry",
        "outputId": "996a070c-952c-40e4-c269-aee42e33d081"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:1: RuntimeWarning: invalid value encountered in arcsin\n",
            "  \"\"\"Entry point for launching an IPython kernel.\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "nan"
            ]
          },
          "execution_count": 164,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "np.arcsin(2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00105-068cb2e2-67f6-4789-8aa9-8df6cb73f631",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "id": "kzkODWkAsUGH",
        "outputId": "27e7fc7c-0357-4d7d-d563-8d91a58bb635"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(1.5707963267948966+1.3169578969248166j)"
            ]
          },
          "execution_count": 165,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "np.arcsin(2+0j)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00106-6259c1ee-9808-4b0a-ac5d-28c2a35c0c03",
        "deepnote_cell_type": "markdown",
        "id": "1CCDk_m0sSH5"
      },
      "source": [
        "`numpy.lib.scimath` imported as `sc` here, is from `sc?`:\n",
        "> Wrapper functions to more user-friendly calling of certain math functions\n",
        "whose output data-type is different than the input data-type in certain\n",
        "domains of the input.\n",
        "Function with some parts of its domain in the complex plane like, `sqrt`, `log`, `log2`, `logn`, `log10`, `power`, `arccos`, `arcsin`, and `arctanh`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00107-d4582586-7946-48c2-b2a1-4e57643deb70",
        "deepnote_cell_type": "code",
        "id": "ujaLOBc440Yt",
        "outputId": "80539b82-7078-4546-c0c7-a01912040bf5"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(1.5707963267948966+1.3169578969248166j)"
            ]
          },
          "execution_count": 166,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "np.lib.scimath.arcsin(2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00108-21fe7bc7-b62e-419e-8f4a-77c5fcb3eeef",
        "deepnote_cell_type": "code",
        "id": "2FfKDp1JXaft",
        "outputId": "7d7f4015-6a81-4259-fd67-71f10375a0e3"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(1.5707963267948966+1.3169578969248166j)"
            ]
          },
          "execution_count": 167,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "sc.arcsin(2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00109-fa35b372-96f9-4949-acbd-3e1dd8b97d6e",
        "deepnote_cell_type": "code",
        "id": "148M2gp0ul3b"
      },
      "outputs": [],
      "source": [
        "import ipywidgets as widgets"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00110-28966f91-cbf3-4e57-9037-3909018ee925",
        "colab": {
          "referenced_widgets": [
            "c7649e6b09e544169692a5bd523dd0d2"
          ]
        },
        "deepnote_cell_type": "code",
        "id": "OgpSHexV40Y0",
        "outputId": "1c74eef5-72ef-43ba-8ba4-7e1a800f6f11",
        "tags": [
          "interactive"
        ]
      },
      "outputs": [
        {
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "c7649e6b09e544169692a5bd523dd0d2",
              "version_major": 2,
              "version_minor": 0
            },
            "text/plain": [
              "interactive(children=(IntSlider(value=1, description='x', max=2), Output()), _dom_classes=('widget-interact',)…"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "@widgets.interact\n",
        "def f(x=(0,2)):\n",
        "    print(np.abs(sc.arcsin(x)))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00111-65b42516-574d-47e8-98f2-bb422c3e958a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 88
        },
        "deepnote_cell_type": "code",
        "id": "3tptBZcLNqBT",
        "outputId": "4e266e8e-f43c-4c0a-cb2a-bbcce4cb402b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "array([1.57079633+1.3169579j , 1.57079633+1.76274717j])"
            ]
          },
          "execution_count": 170,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "sc.arcsin([2,3])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00112-16b90e2f-1770-4f84-b1fd-e1197c7da6ac",
        "deepnote_cell_type": "markdown",
        "id": "WNGKkoW4F_zT"
      },
      "source": [
        "# Lists, Tuples, Dictionaries and Sets"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00113-6ca5b993-d2b8-48df-95e5-92e102a819fc",
        "deepnote_cell_type": "markdown",
        "id": "ACaVyEIMF_zU"
      },
      "source": [
        "## Lists"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00114-8627121b-1169-43dc-8a80-c2b50bc7bc23",
        "deepnote_cell_type": "markdown",
        "id": "8bU3iP8xF_zV"
      },
      "source": [
        "Lists are useful when you want to store and manipulate a set of elements (even of different types)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00115-43993951-a96b-45f5-9aa6-218250de2875",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 19,
        "execution_start": 1627053894891,
        "id": "xWUtR9EUF_zW",
        "outputId": "6526a6f3-1b28-4e2b-e5e4-2b3e346bc37e",
        "source_hash": "f35af975"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['abc', 42, 3.1415]"
            ]
          },
          "execution_count": 11,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#A list is declared using [] and may content different type of objects\n",
        "lista = [\"abc\", 42, 3.1415]\n",
        "lista"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00116-f1ac2a71-cd80-4bdf-b55a-36c96d210522",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 12,
        "execution_start": 1627053528338,
        "id": "HF_XL0MWF_zY",
        "outputId": "3117d2de-db39-4d86-ef4a-e7613bb78ac0",
        "source_hash": "a16ca4d8"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "'abc'"
            ]
          },
          "execution_count": 4,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#First element of the list\n",
        "lista[0]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00117-9bee40ba-69b5-45ad-ac99-ded3cebca55a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 58,
        "execution_start": 1627053562906,
        "id": "wAPJeJnIF_za",
        "outputId": "f173775f-6eec-41b0-e8ad-9b14d218ad61",
        "source_hash": "b4dd55f4"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "3.1415"
            ]
          },
          "execution_count": 5,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Last element of the list\n",
        "lista[-1]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00119-4ee37b8f-4184-4968-9344-ce71d1e7bc47",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 18,
        "execution_start": 1627053898484,
        "id": "Nl-dVEMRF_zc",
        "outputId": "8a371e78-9b6b-41b5-9060-74808cf7cac5",
        "source_hash": "3d493445"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['abc', 42, 3.1415, True]"
            ]
          },
          "execution_count": 12,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Adding a new element (boolean element)\n",
        "lista.append(True)\n",
        "lista"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00120-a12d4510-740e-497c-b699-ffd41b801f67",
        "deepnote_cell_type": "markdown",
        "tags": [],
        "id": "5NxZA8DaXafw"
      },
      "source": [
        "WARNING:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00120-d1e762c2-34ba-43de-807e-59500bcab8ef",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 14,
        "execution_start": 1627053918373,
        "source_hash": "b1a5bc03",
        "tags": [],
        "id": "6XA3sy1xXafw",
        "outputId": "b3286566-9ce5-44ad-d3fb-4112bc47583f"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "None\n"
          ]
        }
      ],
      "source": [
        "newlista=lista.copy()\n",
        "newlista=newlista.append(5)\n",
        "print(newlista)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00120-b066d01c-cfd2-4b88-b396-acaa67bae085",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 13,
        "execution_start": 1627053977167,
        "id": "SevBLsrgF_ze",
        "outputId": "70424d0e-4239-4a2a-f653-ee168140e1c2",
        "source_hash": "9186f96e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['abc', 'I am second', 42, 3.1415, True]"
            ]
          },
          "execution_count": 14,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Inserting a new second element \n",
        "lista.insert(1, \"I am second\")\n",
        "lista"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00121-8b9c757b-9fb4-4610-b94e-ac2f7ae4e869",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 10,
        "execution_start": 1627054016142,
        "id": "nSHDnC2AF_zg",
        "outputId": "0116348f-b350-4c54-a5e5-ff02641c31e6",
        "source_hash": "8aee6b76"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['abc', 'I am second', 42, True]"
            ]
          },
          "execution_count": 15,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Deleting the third element of the list\n",
        "del lista[3]\n",
        "lista"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00122-ffe7df5c-b2da-45ce-bb94-f432ea290b6d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 39,
        "execution_start": 1627054037210,
        "id": "vlX6FjRkF_zj",
        "outputId": "79a878cc-ee51-43b0-f668-712c487dd005",
        "source_hash": "b6a109d0"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['xyz', 'I am second', 42, True]"
            ]
          },
          "execution_count": 16,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Reassign the first element of the list\n",
        "lista[0] = \"xyz\"\n",
        "lista"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00123-57f91b00-6a13-4568-a840-c95e04b50c68",
        "deepnote_cell_type": "markdown",
        "id": "pfNBq-Bj40ZQ"
      },
      "source": [
        "### Slicing: \n",
        "Extract elements from a list, `l` from one given index to another given index. We pass slice instead of index like this: \n",
        "```python3\n",
        "l[start:end]\n",
        "```\n",
        "We can also define the step, like this: \n",
        "```python3\n",
        "l[start:end:step]\n",
        "```\n",
        "If `start` is not passed it is considered 0. If `end` is not passed it is considered length of array in that dimension. The `end` can given in reverse order by assigning a minus signus to the index. For example `-1` means the last element, while `-2` means the penultimate, and so on and so forth."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00124-4673fb4b-69a6-44c5-b553-b29ecda18ed3",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 9,
        "execution_start": 1627054210718,
        "id": "rCgwPFIgF_zl",
        "outputId": "81c27ad4-596f-41de-af83-73d69871889d",
        "source_hash": "5d30bd51"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['xyz', 'I am second', 42]"
            ]
          },
          "execution_count": 17,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Showing the elements from 0 to 2\n",
        "lista[0:3]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00125-f058494c-bb47-4974-93c6-7cb70b3650c3",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 25,
        "execution_start": 1627054240750,
        "id": "7EnY5Z_A40ZT",
        "outputId": "58fe6bbe-5014-4c96-8d55-0ccb52aad24b",
        "source_hash": "d90acb3b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[42, True]"
            ]
          },
          "execution_count": 18,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Showing the last two elements\n",
        "lista[-2:]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00126-2c6edb8f-e21a-4c78-bbf8-911ef5d1be11",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 10,
        "execution_start": 1627054255404,
        "id": "hFTEHeueF_zn",
        "outputId": "8abb0632-4243-4422-8a86-2df841e0a81e",
        "source_hash": "8f046dad"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['xyz', 42]"
            ]
          },
          "execution_count": 19,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Showing elements two by two\n",
        "lista[::2]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00127-088529a1-cdd2-4f2c-a55f-97c24a554d43",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 57,
        "execution_start": 1627054269516,
        "id": "AmtfO6SE40Zb",
        "outputId": "ab306330-6683-401a-d637-ab84747d0b96",
        "source_hash": "9349264f"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[True, 42, 'I am second', 'xyz']"
            ]
          },
          "execution_count": 20,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Reverse order\n",
        "lista[::-1]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00128-f3e96f1b-30fb-4dc6-8cf5-10f8c0a3bdac",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 14,
        "execution_start": 1627054333990,
        "source_hash": "8a17b22b",
        "id": "Mayng4SLXafy",
        "outputId": "70fe061d-b418-4286-cea4-7ecca95a9c65"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[True, 42, 'I am second', 'xyz']"
            ]
          },
          "execution_count": 22,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "lista"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00129-d0c2f7e2-f0b2-492e-9204-dc38f3b0c8d7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 10,
        "execution_start": 1627054348910,
        "id": "JtdcF2L540Ze",
        "outputId": "63ec49e9-57e7-47e7-96fe-81373736226e",
        "source_hash": "871441e4"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['xyz', 'I am second', 42, True]"
            ]
          },
          "execution_count": 23,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#also as\n",
        "lista.reverse()\n",
        "lista"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00130-1315bac9-04c4-4e12-bd71-e54c9c188e09",
        "deepnote_cell_type": "markdown",
        "id": "-nwqd5OH40Zh"
      },
      "source": [
        "### Embedded lists"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00131-aaab6b1e-dcd6-448d-9c9c-c58f8a2df353",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 10,
        "execution_start": 1627054580810,
        "id": "FZOAGZujF_zp",
        "outputId": "fd8d4e2d-ca8d-4779-8a48-a8a9b7acf435",
        "source_hash": "a0121d4d"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[['xyz', 'I am second', 42, True], [True, 42]]"
            ]
          },
          "execution_count": 24,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#It is possible to embed a list\n",
        "embedded_list = [lista, [True, 42]]\n",
        "embedded_list"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00132-57f0bd10-d081-42bd-992b-712686faa210",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 12,
        "execution_start": 1627054613548,
        "id": "jYQgFdOYF_zr",
        "outputId": "8bb6ca52-7c21-4b9e-b2de-30005c8420ca",
        "source_hash": "693c0cdf"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "'I am second'"
            ]
          },
          "execution_count": 25,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#Second element of the first list\n",
        "embedded_list[0][1]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00133-9df3b1ce-f6c3-4be5-b737-949607db44c0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 14,
        "execution_start": 1627055234675,
        "id": "uyw-E8VoF_zt",
        "outputId": "12473d6c-92e8-491f-a61a-31edcf459253",
        "source_hash": "d11f70fc"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[[1, 2], [3, 4]]"
            ]
          },
          "execution_count": 36,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#A matrix as a list of embedded lists\n",
        "A = [ [1,2], [3,4] ]\n",
        "A"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00134-e1d5ee2c-0fe9-46c2-85ce-0762e05611bc",
        "deepnote_cell_type": "markdown",
        "id": "BYpSrRqlgX6j"
      },
      "source": [
        "**Activity**: Obtain entry $A_{01}$ of the previous matrix, where\n",
        "$$\n",
        "A=\\begin{pmatrix}\n",
        "A_{00} & A_{01}\\\\\n",
        "A_{10} & A_{11}\\\\\n",
        "\\end{pmatrix}\n",
        "$$"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00135-f5b3c211-9abc-4c21-8806-2f1c4a1e2b14",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 0,
        "execution_start": 1627060206310,
        "id": "jisAwrcf40Zq",
        "source_hash": "b623e53d"
      },
      "outputs": [],
      "source": [
        ""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00136-243850cf-39b5-4c5d-842f-72e235c72269",
        "deepnote_cell_type": "markdown",
        "id": "xou55DH140Zs"
      },
      "source": [
        "### Sum of lists"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00137-d0e5120c-94d6-40e3-8979-a9bdb0bf0794",
        "deepnote_cell_type": "code",
        "id": "DDYA-n0pF_zv",
        "outputId": "6c19cc81-1d0c-46df-ffdc-666d29e1cd30"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[1, 2, 'ab', True, [1, 2], 3.1415, 'Pi', 'circle']"
            ]
          },
          "execution_count": 45,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#When two list are added, the result is a new concatenated list\n",
        "[1,2,\"ab\",True,[1,2]] + [3.1415,\"Pi\",\"circle\"]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00138-dc6980e6-fb8f-4a83-b98f-9bc41e9fa01d",
        "deepnote_cell_type": "markdown",
        "id": "mnXJphqAhSpu"
      },
      "source": [
        "**Activity** Add a third row with integer values to the previous $A$ matrix\n",
        "<!-- Answer: A=A+[[5,6]] -->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00139-5b796ccf-fa09-400b-91e8-ef347d747586",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 0,
        "execution_start": 1627060219998,
        "id": "cDjXm_LthoWk",
        "source_hash": "b623e53d"
      },
      "outputs": [],
      "source": [
        ""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00140-ede7d349-571e-42fe-b4f5-0963810a6e95",
        "deepnote_cell_type": "markdown",
        "id": "7QgsQSv2F_zy"
      },
      "source": [
        "An additional ingredient is the `append` method of a Python list. It update the elements of the list without update explicitly the variable with some equal reasignment."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00141-cd443c5b-58be-4308-8fd1-7c9c87b2ba35",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 1,
        "execution_start": 1627055372390,
        "id": "ZxLgIuS7F_zy",
        "outputId": "2d347140-f163-46ea-d925-1989cbb6f033",
        "source_hash": "a8e6b8c3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "after append 2 to [] : [2]\n",
            "after append 5 to [2]: [2, 5]\n"
          ]
        }
      ],
      "source": [
        "y=[]\n",
        "y.append(2)\n",
        "print(f'after append 2 to [] : {y}')\n",
        "y.append(5)\n",
        "print(f'after append 5 to [2]: {y}')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00144-953af19d-ca28-4a4e-bee2-d74b5a2ed2bc",
        "deepnote_cell_type": "markdown",
        "tags": [],
        "id": "019LL1LiXaf2"
      },
      "source": [
        "functions to generate lists:\n",
        "* `range`\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00145-0c5d3016-156c-451f-932f-8f9f85498c7c",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 16,
        "execution_start": 1627055526138,
        "source_hash": "f94a8b9f",
        "tags": [],
        "id": "zX244g8bXaf2",
        "outputId": "d54d664d-9ed0-44d5-b4ca-778199501322"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[0, 1, 2]"
            ]
          },
          "execution_count": 40,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "list(range(3))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00146-849cc4fe-5da8-4d42-90c7-a9af3c9a6bf3",
        "deepnote_cell_type": "markdown",
        "tags": [],
        "id": "D5g8L9unXaf2"
      },
      "source": [
        "Conditional in lists:\n",
        "* `in`\n",
        "* `any`\n",
        "* `all`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00147-8be3f9a4-90f7-4d7d-8f26-0d2ed226b968",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 37,
        "execution_start": 1627060569158,
        "source_hash": "fffd76d",
        "tags": [],
        "id": "a-3ZLrVUXaf2",
        "outputId": "5ff0eaa6-caa1-4216-8825-2c9f6bb1fd9e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 58,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "3 in [4,5,6]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00148-c0099d37-13a9-4cd4-956f-615e5ec21d29",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 30,
        "execution_start": 1627061227281,
        "source_hash": "f97063ef",
        "tags": [],
        "id": "p0Tws8yeXaf3",
        "outputId": "fccf67f4-5d09-4886-c26c-dd1f8554c299"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 60,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "any([False,False,False])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00149-722ef06e-9a14-499f-b6a5-0327a0f3b25f",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 27,
        "execution_start": 1627061259749,
        "source_hash": "95cdbf30",
        "tags": [],
        "id": "XmH-yUisXaf3",
        "outputId": "a73ee5a2-c7d5-407c-d403-90a2eb94d25d"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 61,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "any([False,False,True])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00150-457d1a36-ff2e-4536-9ed8-93f5a576d699",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 42,
        "execution_start": 1627061327173,
        "source_hash": "53e77c51",
        "tags": [],
        "id": "UmMwDo7JXaf3",
        "outputId": "f068b06e-a777-48c0-8449-ed1ef1fceeef"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 62,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "all([False,False,True])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00151-c4913ce3-2f69-403f-bfcb-ae8ad7b6bcdb",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 83,
        "execution_start": 1627061347380,
        "source_hash": "2b9de73e",
        "tags": [],
        "id": "acIFfE3VXaf3",
        "outputId": "a4859376-691b-41e8-9c87-2a08232eaf9c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 63,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "all([True,True,True])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00142-f1e3f95e-52a8-4546-9dfb-e628aee03dad",
        "deepnote_cell_type": "markdown",
        "id": "n5PCnFO3F_z1"
      },
      "source": [
        "### List Comprehensions"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00143-cd725699-69ce-4b14-9331-fc3e1b984d0e",
        "deepnote_cell_type": "markdown",
        "id": "mels66d2F_z2"
      },
      "source": [
        "Taken from [here](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions): List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00144-d03421d8-09dd-4c54-95fc-ff2e296eb5d3",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 12,
        "execution_start": 1627055611742,
        "id": "o0BpeNa0F_z3",
        "outputId": "0e0430f6-1453-4001-c042-0d0af3ebece2",
        "source_hash": "53b8c8a9"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"
            ]
          },
          "execution_count": 41,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "[x**2 for x in range(10)]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00149-1607ced4-e77c-40b9-b275-24353bfaf291",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 11,
        "execution_start": 1627056290818,
        "source_hash": "b593dd3d",
        "tags": [],
        "id": "xx4isQoCXaf4",
        "outputId": "17b324fe-d2fc-4dcc-a7a1-191d3553a7b5"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[4, 16, 36, 64]"
            ]
          },
          "execution_count": 56,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "[x**2 for x in range(2,10,2)]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00145-27cc9103-afe6-4897-ab89-e7e1d0f34741",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 21,
        "execution_start": 1627055632524,
        "id": "AQW_kdviF_z5",
        "outputId": "893ef954-32f9-4822-ccce-55fafdb21f8d",
        "source_hash": "ffd3f664"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[[1, 3], [1, 4], [2, 3], [2, 1], [2, 4], [3, 1], [3, 4]]"
            ]
          },
          "execution_count": 42,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "[[x, y] for x in [1,2,3] for y in [3,1,4] if x != y]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00146-be9ef7b8-23ce-4681-94cb-53e349445bb7",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 6,
        "execution_start": 1627055660948,
        "id": "2Zl1DwNy40Z7",
        "source_hash": "2b33c16d"
      },
      "outputs": [],
      "source": [
        "l=[ ['A','B','C'],['D','E','F'],['G','H','I']  ]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00147-e91196c0-77fc-4b30-a17c-9617e71f5937",
        "deepnote_cell_type": "markdown",
        "id": "MMPgcuo_40Z-"
      },
      "source": [
        "we can extract the list that contains `'H'`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00153-0cf5909e-7024-4676-a97b-770f9e396b18",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 14,
        "execution_start": 1627055872147,
        "source_hash": "8e79fb42",
        "tags": [],
        "id": "x7HgibzZXaf5",
        "outputId": "4aeb10cd-9711-474c-ef93-611133f89278"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[['G', 'H', 'I']]"
            ]
          },
          "execution_count": 46,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "[ll for ll in l if 'H' in ll]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00154-b8a38b7b-ceca-4e7b-9251-b920e7ba902c",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 10,
        "execution_start": 1627055957594,
        "source_hash": "7a5cfca9",
        "tags": [],
        "id": "oDAdiMAWXaf5",
        "outputId": "a6c0bcc6-652f-4ba8-be25-c55b352a476b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 49,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "'H' in l"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00154-592b9433-ca61-4ddc-b70d-23fab88c4d11",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 14,
        "execution_start": 1627055938471,
        "source_hash": "c3ba2c1d",
        "tags": [],
        "id": "_z1KGrMaXaf5",
        "outputId": "dbad103c-bd3e-4889-aca9-267bbc940a39"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 48,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "['G','H','I'] in l"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00149-ba2b3d50-e292-42a0-b183-849aad668e48",
        "deepnote_cell_type": "markdown",
        "id": "J0-SP0qP40aB"
      },
      "source": [
        "### Reversed comprehension\n",
        "We can use the method `reversed(...)` to generate an iterator with the revesersed list so that the original list is kept."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00150-a8e26da0-94cf-4991-8a4a-f7ed1dd218d2",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 15,
        "execution_start": 1627056013024,
        "source_hash": "8a17b22b",
        "id": "VG9rc6kdXaf6",
        "outputId": "95c4714e-0625-4ef7-c36d-4fe640328ab8"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['xyz', 'I am second', 42, True]"
            ]
          },
          "execution_count": 50,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "lista"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00151-c5f30d41-9775-4dbb-a741-bd2947f8f444",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 0,
        "execution_start": 1627056026414,
        "id": "1XNRSTG040aF",
        "outputId": "9b66acdf-9bb9-48e7-9fbc-4ed653e4afbd",
        "source_hash": "ec1b4107"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "reversed: [True, 42, 'I am second', 'xyz']\n",
            "original: ['xyz', 'I am second', 42, True]\n"
          ]
        }
      ],
      "source": [
        "print('reversed: {}'.format( list(reversed(lista)) ))\n",
        "print('original: {}'.format(lista))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00152-794b53b9-d350-4b65-857c-d49bb9da22f0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "id": "6HxZreij_5tu",
        "outputId": "0816d6ef-5ecb-4818-ec50-081a7239a22a"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['xyz', 'I am second', 42, True]"
            ]
          },
          "execution_count": 33,
          "metadata": {
            "tags": []
          },
          "output_type": "execute_result"
        }
      ],
      "source": [
        ""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00153-98fee61f-e155-45ea-ae9a-59845ba49a0a",
        "deepnote_cell_type": "markdown",
        "id": "txgjCoaIF_z7"
      },
      "source": [
        "## Tuples"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00154-5a0084bd-f33e-47e1-a5a1-3e513e36368a",
        "deepnote_cell_type": "markdown",
        "id": "OtJzxOFtF_z8"
      },
      "source": [
        "A tuple is almost equal to a list, except that once declared its elements, it is not possible to modify them. Therefore, tuples are useful only when you want to store some elements but not modify them."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00155-256f5c89-6a1b-474d-91c2-982e7bb4f433",
        "deepnote_cell_type": "code",
        "id": "f3skilG2F_z8",
        "outputId": "1b1ba135-88ba-4bbd-a489-29b6458a45f7"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "('abc', 42, 3.1415)"
            ]
          },
          "execution_count": 65,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#A tuple is declared using ()\n",
        "tupla = (\"abc\", 42, 3.1415)\n",
        "tupla"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00156-44f08913-fa8d-45ad-b1b7-29bfec4bcdd6",
        "deepnote_cell_type": "markdown",
        "id": "uhv7dS2Q-2uh"
      },
      "source": [
        "Note: single element tuple"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00157-0bf093c5-fcd7-4037-bebf-e6da8d4a84c6",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 1,
        "execution_start": 1627056061261,
        "source_hash": "36ea1d96",
        "id": "Ki9FvVceXaf_",
        "outputId": "8a00ae30-3dc5-4434-8139-e254ba5ee23e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "execution_count": 52,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "(2) #equivalent to 2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00158-e728a1f9-7751-45e2-8143-436b36f676b8",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 4,
        "execution_start": 1627056074298,
        "id": "gZlzseaI-8Xm",
        "source_hash": "fc89a494"
      },
      "outputs": [],
      "source": [
        "t=(2,)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00159-ad542ff7-19c9-4aff-99a3-baac96e5ecb1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "id": "Fu11CK1L_TYA",
        "outputId": "d691f670-c11c-4882-9a1b-143b48853075"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "1"
            ]
          },
          "execution_count": 68,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "len(t)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00160-b811c8ab-f84a-46b9-bc19-fb607985fbfc",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 166
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 18,
        "execution_start": 1627056079374,
        "id": "slJ7Lrfh_XAb",
        "outputId": "17090d2e-f4c0-43ac-e1fd-ddf02e26df1c",
        "source_hash": "5a4849fa"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "execution_count": 54,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "t[0]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00161-3f420b93-2467-4cd1-a97b-15b274dcc657",
        "deepnote_cell_type": "markdown",
        "id": "x3M6C67140aW"
      },
      "source": [
        "The comprenhension tuple also works"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00162-a415fe35-389c-414c-a715-b680e65d3f41",
        "deepnote_cell_type": "code",
        "id": "PYlzClDB40aX",
        "outputId": "c10f27e1-fb96-4760-9ab9-0eafcdb55a03"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "('abc', 42, 3.1415)"
            ]
          },
          "execution_count": 71,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "tuple( (t for t in tupla)  )"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00163-6ec69b7f-7fc2-451e-9672-7a13487adb97",
        "deepnote_cell_type": "markdown",
        "id": "gh7KXCGH40aa"
      },
      "source": [
        "`any` can extract a true value from a comprension tuple (see also `all`: https://docs.python.org/3/library/functions.html#all). \n",
        "In fact, for the following nested list:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00164-358dc760-b8e8-4585-bfcd-93d6241b7144",
        "deepnote_cell_type": "code",
        "id": "gM2YlwEF40aa"
      },
      "outputs": [],
      "source": [
        "l=[ ['A','B','C'],['D','E','F'],['G','H','I']   ]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00165-7820b06a-4910-4efd-90d2-37e9738bbef6",
        "deepnote_cell_type": "markdown",
        "id": "-3ZrGX6K40ac"
      },
      "source": [
        "we can extract the list that contains `'H'` more easily"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00166-1f463c7a-074e-42be-ae04-2d4f44be198d",
        "deepnote_cell_type": "code",
        "id": "q9fyyNVxXagB",
        "outputId": "5852980b-c844-4276-fc57-c1654287ac9c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]"
            ]
          },
          "execution_count": 78,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "[ll for ll in l]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00167-0a3f82b7-bcab-4f03-ae92-8a3f1a450853",
        "deepnote_cell_type": "code",
        "id": "V4r4E4lQXagB",
        "outputId": "033b96c8-3ed0-4499-aa5c-6a7ee9c5440e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 82,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "any((s=='L' for s in ['G', 'H', 'I']))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00168-14ee9a7d-a062-410d-b932-0eab109beac8",
        "deepnote_cell_type": "code",
        "id": "_ltlDGMz40ad",
        "outputId": "44950aec-0c22-4bf9-c442-9f22dfc3ec6a"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[['G', 'H', 'I']]"
            ]
          },
          "execution_count": 83,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "[ll for ll in l if any( s=='H' for s in ll  ) ]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00169-803fda79-7313-4eaa-b867-b4748e3bb3b1",
        "deepnote_cell_type": "markdown",
        "id": "J9rPXb0a40ag"
      },
      "source": [
        "With the function `zip` we can generate dictionary-like tuple from two lists:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00170-3a093a73-05f4-40ee-82b8-8bc36637618b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "id": "13619Vve_qNE",
        "outputId": "ce6b81b4-c6e0-4a88-ef7b-f383e55d730a"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[('A', 1), ('B', 2), ('C', 3)]"
            ]
          },
          "execution_count": 86,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "list(zip( ['A','B','C'],[1,2,3]  ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00171-0474af69-315e-402d-8775-19f56274b0ef",
        "deepnote_cell_type": "code",
        "id": "qVT1k-en40ag",
        "outputId": "96f56944-57cc-471c-c16f-857aa41e2377"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[('A', 1), ('B', 2), ('C', 3)]"
            ]
          },
          "execution_count": 85,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "list(zip( ['A','B','C'],[1,2,3]  ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00172-928ae2c5-c92b-4ec5-b7ff-d3c8195dc2f9",
        "deepnote_cell_type": "code",
        "id": "uAiixodKF_z-",
        "outputId": "4e199236-94c9-486f-a792-956923d3f6d5"
      },
      "outputs": [
        {
          "ename": "AttributeError",
          "evalue": "'tuple' object has no attribute 'append'",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-87-4cc56b436273>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#It is not possible to add more elements\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mtupla\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"xy\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mAttributeError\u001b[0m: 'tuple' object has no attribute 'append'"
          ]
        }
      ],
      "source": [
        "#It is not possible to add more elements\n",
        "tupla.append(\"xy\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00173-b004a635-74e6-4739-88a8-ffab9d845090",
        "deepnote_cell_type": "code",
        "id": "GiY-kyfHF_0A",
        "outputId": "76c602ca-e8f6-4608-fd5a-dff8cfdaf7a4"
      },
      "outputs": [
        {
          "ename": "TypeError",
          "evalue": "'tuple' object doesn't support item deletion",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-88-c05ec550c1d0>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#It is not possible to delete an element\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;32mdel\u001b[0m \u001b[0mtupla\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: 'tuple' object doesn't support item deletion"
          ]
        }
      ],
      "source": [
        "#It is not possible to delete an element\n",
        "del tupla[0]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00174-30f10522-e562-422a-af00-376cce233822",
        "deepnote_cell_type": "code",
        "id": "jwJPysSkF_0D",
        "outputId": "f99022e1-245d-4534-fa4f-b4584786e768"
      },
      "outputs": [
        {
          "ename": "TypeError",
          "evalue": "'tuple' object does not support item assignment",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-89-4e97d1641827>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#It is not possible to modify an existing element\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mtupla\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"xy\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
          ]
        }
      ],
      "source": [
        "#It is not possible to modify an existing element\n",
        "tupla[0] = \"xy\""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00175-acb86315-216f-43fd-b3f1-6b1d62f8e1ee",
        "deepnote_cell_type": "markdown",
        "id": "rafwug2SF_0F"
      },
      "source": [
        "## Dictionaries"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00176-0dee92e2-0919-4509-ab7b-8c4ae026afe2",
        "deepnote_cell_type": "markdown",
        "id": "7vlLjdVRF_0G"
      },
      "source": [
        "Dictionaries are labeled lists: with keys and values. They are extremely useful when manipulating complex data. In Wolfram Alpha the equivalent object is called [Associations](https://reference.wolfram.com/language/guide/Associations.html)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00177-2aad3f22-aeba-4264-9e09-82f40f9a9052",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 55
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 10,
        "execution_start": 1628262626619,
        "id": "vUXMEigkF_0G",
        "outputId": "c806d219-32bd-40f9-bbc6-16102e4514ef",
        "source_hash": "7abfe7bf"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Kenia': 'Nairobi', 'Noruega': 'Oslo', 'Finlandia': 'Helsinski', 'Rusia': 'Moscú', 'Rio de Janeiro': 'Rio', 'Japón': 'Tokio', 'Colorado': 'Denver', 'Alemania': 'Berlin', 'Colombia': 'Bogotá'}\n"
          ]
        }
      ],
      "source": [
        "#A dictionary is declared using {}, and specifying the name of the component, then the character : followed by the element to store.\n",
        "dictionary={ 'Kenia'         :'Nairobi',\n",
        "             'Noruega'       :'Oslo',\n",
        "             'Finlandia'     :'Helsinski',\n",
        "             'Rusia'         :'Moscú',\n",
        "             'Rio de Janeiro':'Rio',\n",
        "             'Japón'         :'Tokio',\n",
        "             'Colorado'      :'Denver',\n",
        "             'Alemania'      :'Berlin',\n",
        "             'Colombia'      :'Bogotá'}\n",
        "print(dictionary)\n",
        "#Note the order in a dictionary does not matter as one identifies a single element through a string, not a number"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00178-f0530215-2bee-40ff-b000-f658b73c3fa9",
        "deepnote_cell_type": "markdown",
        "id": "IWoHFWTx40av"
      },
      "source": [
        "Instead of a number, an element of a dictionary is accessed with the key of the component"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00179-cf329bd3-ad70-480b-bbad-53f885000c47",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 17,
        "execution_start": 1628262629960,
        "source_hash": "1dd6b4f7",
        "id": "vdthcTo1XagE",
        "outputId": "62fdfaff-9f02-43ba-e616-8aefa7d5031e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{'Kenia': 'Nairobi',\n",
              " 'Noruega': 'Oslo',\n",
              " 'Finlandia': 'Helsinski',\n",
              " 'Rusia': 'Moscú',\n",
              " 'Rio de Janeiro': 'Rio',\n",
              " 'Japón': 'Tokio',\n",
              " 'Colorado': 'Denver',\n",
              " 'Alemania': 'Berlin',\n",
              " 'Colombia': 'Bogotá'}"
            ]
          },
          "execution_count": 3,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "dictionary"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00180-03d84b01-c18b-4ff8-ba65-fab7292576b3",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "id": "bVHKdCigF_0K",
        "outputId": "0cd39b16-fb1d-4a41-d079-ea099257efb8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Tokio ♥ Rio\n"
          ]
        }
      ],
      "source": [
        "print('{} ♥ {}'.format( dictionary['Japón'], dictionary['Rio de Janeiro']) )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00181-721e1c8d-559d-4dec-9f51-16f1b699838c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 54,
        "execution_start": 1628262732927,
        "id": "QK-1FnAnF_0M",
        "outputId": "da43655e-b6f8-4740-e3cc-c0cb430fd4e6",
        "source_hash": "e6b0b2a6"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Azul\n"
          ]
        }
      ],
      "source": [
        "#The elements of the dictionary may be of any type\n",
        "dictionary2 = { \"Enteros\":[1,2,3,4,5], \n",
        "                \"Ciudad\" :\"Medellin\", \n",
        "                \"Cédula\" :1128400433, \n",
        "                \"Colores\":[\"Amarillo\", \"Azul\", \"Rojo\"] }\n",
        "print(dictionary2[\"Colores\"][1])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00182-b05c88f3-8661-4d19-8786-4b6480f96ffb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_start": 1628262776687,
        "id": "j5epa2zcF_05",
        "outputId": "49dc833e-cff1-4990-c933-250c75072679",
        "source_hash": "7b0dd9f0"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Enteros': [1, 2, 3, 4, 5], 'Ciudad': 'Bogota', 'Cédula': 1128400433, 'Colores': ['Amarillo', 'Azul', 'Rojo']}\n"
          ]
        }
      ],
      "source": [
        "#The elements of the dictionary can be modified only by changing directly such an element\n",
        "dictionary2[\"Ciudad\"] = \"Bogota\"\n",
        "print(dictionary2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00183-98bdbade-02ef-4c96-9274-7cdf846e87a9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 55
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 0,
        "execution_start": 1628262810808,
        "id": "fTtrGPXsF_08",
        "outputId": "b4eb22a4-2f18-4761-aafa-2b90be7e8041",
        "source_hash": "bb0e866d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Enteros': [1, 2, 3, 4, 5], 'Ciudad': 'Bogota', 'Cédula': 1128400433, 'Colores': ['Amarillo', 'Azul', 'Rojo'], 'Pais': 'Colombia', 'País': 'Chile'}\n"
          ]
        }
      ],
      "source": [
        "#Adding a new element is possible by only defining the new component\n",
        "dictionary2[\"Pais\"] = \"Colombia\"\n",
        "dictionary2[\"País\"] = \"Chile\"\n",
        "print( dictionary2 )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00184-4935b754-28ed-45b9-bfbf-4d87d820ddd9",
        "deepnote_cell_type": "code",
        "id": "qhMqpewqkxaF"
      },
      "outputs": [],
      "source": [
        "#dictionary2.update({'Pais':'Colombia'})"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00198-08eff87f-6fa8-44b6-be20-20e993a3bb7e",
        "deepnote_cell_type": "markdown",
        "tags": [],
        "id": "jubURLY5XagG"
      },
      "source": [
        "List-like dictionary"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00199-79ff680b-ea8f-4894-903f-1e662b463163",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 13,
        "execution_start": 1628262965489,
        "source_hash": "63b2cce9",
        "tags": [],
        "id": "jogoVkrcXagG",
        "outputId": "7cfa5442-15df-4936-fc14-d81b87df7ac7"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "45"
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "l={0:45,1:345,2:987}\n",
        "l[0]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00200-12fd4aac-1894-4ddb-a7fc-4df171c6deef",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 5,
        "execution_start": 1628263125325,
        "source_hash": "b7fc3f07",
        "tags": [],
        "id": "SVd64KjGXagG"
      },
      "outputs": [],
      "source": [
        "l={0.3:45}"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00201-7e3b1869-8cd3-4be6-b7b4-c660839ad1ac",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 13,
        "execution_start": 1628263144179,
        "source_hash": "662f52b",
        "tags": [],
        "id": "aP482f7kXagH",
        "outputId": "d2148663-34b0-4364-d218-339ccb31804b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "45"
            ]
          },
          "execution_count": 13,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "l[0.3]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00202-43aafd17-e1b3-4041-968f-5c5aac384a40",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 14,
        "execution_start": 1628263189146,
        "source_hash": "7217c2d4",
        "tags": [],
        "id": "hM6OM-fJXagH",
        "outputId": "2ea9eb88-4cd7-4572-ede4-f8d78a89e56b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "'Verdadero'"
            ]
          },
          "execution_count": 15,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "d={True:'Verdadero'}\n",
        "d[True]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00185-dd7f8b7a-a84c-43cc-94bf-920eff10ceed",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 10,
        "execution_start": 1628263226763,
        "id": "X3Knds5oF_0_",
        "outputId": "41cd14f7-f549-49e6-ff3c-97cece9c2481",
        "source_hash": "1bb3d1ae"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Enteros': [1, 2, 3, 4, 5], 'Ciudad': 'Bogota', 'Cédula': 1128400433, 'Colores': ['Amarillo', 'Azul', 'Rojo'], 'País': 'Chile'}\n"
          ]
        }
      ],
      "source": [
        "#The command del can be also used for deleting an element, as a list\n",
        "del dictionary2[\"Pais\"]\n",
        "print(dictionary2)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00186-8e520c46-2726-484a-84d8-e27f8d5b912f",
        "deepnote_cell_type": "markdown",
        "id": "U51G2o8M40a7"
      },
      "source": [
        "With the previous `zip` function to create tuples from lists, we can create a dictionary from the two lists:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00205-ad5efcef-41d1-4613-8439-a0b2ee077304",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 13,
        "execution_start": 1628263341184,
        "source_hash": "27b839db",
        "tags": [],
        "id": "dYJzRFLSXagH",
        "outputId": "4d23bab0-343a-4d3d-efd1-20fe12c0573a"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[('A', 1), ('B', 2), ('C', 3)]"
            ]
          },
          "execution_count": 21,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "list(zip( ['A','B','C'],[1,2,3]  ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00187-ac485a4d-8749-4147-9498-5b3df3fdeb78",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 21,
        "execution_start": 1628263330801,
        "id": "h_mODhqZ40a7",
        "outputId": "b42b9750-6b54-4eae-d225-c175fcdcf28a",
        "source_hash": "98167189"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{'A': 1, 'B': 2, 'C': 3}"
            ]
          },
          "execution_count": 20,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "dict(zip( ['A','B','C'],[1,2,3]  ))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00188-7ad8d760-6220-48a9-bcff-9e5a1b3535bd",
        "deepnote_cell_type": "markdown",
        "id": "LxMk7Iq3kAJm"
      },
      "source": [
        "**Activity**: Creates a diccionary for the values: `['xyz',3,4.5]` with integer keys starting with zero. In this way, the dictionary could behave as list"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00189-3ef32f75-5897-4dc1-872a-d7815babd6bb",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 5,
        "execution_start": 1628263759228,
        "id": "UKRSPIQe40a9",
        "source_hash": "84df6609"
      },
      "outputs": [],
      "source": [
        "l={}\n",
        "l[0]='xyz'\n",
        "l[1]=3\n",
        "l[2]=4.5"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00190-08da3f14-2724-4e9a-b9a9-ef38ce793782",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 11,
        "execution_start": 1628263387141,
        "source_hash": "66e02963",
        "id": "WmeKomR5XagI",
        "outputId": "dfe8a08b-5348-46c8-fff1-5dc2499f0ed9"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{0: 'xyz', 1: 3, 2: 4.5}"
            ]
          },
          "execution_count": 23,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "l"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00191-01697720-d3a4-40af-9ad9-db96ad98c5cf",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 15,
        "execution_start": 1628263800144,
        "source_hash": "6920433c",
        "id": "EDd9y0cRXagI",
        "outputId": "89854be2-43d7-452e-e590-240492664f7f"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "'xyz'"
            ]
          },
          "execution_count": 30,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "l[0]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00211-57a55c71-25d6-45f4-acd2-a9ebb5986e2a",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 3,
        "execution_start": 1628263803460,
        "source_hash": "1d408dfc",
        "tags": [],
        "id": "0s4ym4I-XagJ"
      },
      "outputs": [],
      "source": [
        "l.get(3)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00206-924ed65c-1523-4caa-a508-2189973fbfb5",
        "deepnote_cell_type": "markdown",
        "tags": [],
        "id": "sp98DGQPXagJ"
      },
      "source": [
        "### Non-relational databases\n",
        "A list of dictionaries is simple example of a non-relational database. Their main advantage is that with the proper glosary for the keys of the dictionaries the data analysis is well expressed through the impledmented code"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00207-42f59028-7745-4a48-8040-90954edb5d78",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 1,
        "execution_start": 1628263979443,
        "source_hash": "1bba42f3",
        "tags": [],
        "id": "V8rGd08zXagJ"
      },
      "outputs": [],
      "source": [
        "people=[{'name':'Juan',  'last_name':'Valdez','age':25},\n",
        "        {'name':'Álvaro','last_name':'Uribe', 'age':69}\n",
        "       ]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00208-faf835dd-994f-497c-8138-61e65fe4c29f",
        "deepnote_cell_type": "markdown",
        "tags": [],
        "id": "4h4CjuLUXagJ"
      },
      "source": [
        "Extract the last names from the `people` data base (Note the very expressive sintaxis!)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00209-2a51149d-f947-4107-bbd9-6afa6881ecd9",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 14,
        "execution_start": 1628263982113,
        "source_hash": "2606fa3f",
        "tags": [],
        "id": "6nEp_Uv-XagJ",
        "outputId": "07513141-d2f6-4292-ba1e-7954c2d13be5"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['Valdez', 'Uribe']"
            ]
          },
          "execution_count": 37,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "[d.get('last_name') for d in people]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00210-46baa099-4abe-486c-8b35-8bc442826702",
        "deepnote_cell_type": "markdown",
        "tags": [],
        "id": "jAA6JEKsXagJ"
      },
      "source": [
        "Sum the ages"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00211-cb9b466e-e45a-4de4-b98b-8f313026df6a",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 55,
        "execution_start": 1627063246851,
        "source_hash": "dc263bbf",
        "tags": [],
        "id": "xTtAu8CJXagK",
        "outputId": "961893ce-431d-42c8-b1ab-b1f04515eb7b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "94"
            ]
          },
          "execution_count": 69,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "sum([d.get('age') for d in people])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00194-4b3af145-7feb-45c8-8c51-c7ffa719210f",
        "deepnote_cell_type": "markdown",
        "tags": [],
        "id": "vVlJDeXWXagK"
      },
      "source": [
        "### Sets"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00195-591e8c38-1833-4206-96c8-f0c6d9b7a54f",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 10,
        "execution_start": 1628264118499,
        "source_hash": "c59caa7b",
        "tags": [],
        "id": "VTr6GFi0XagK",
        "outputId": "df7126f2-48e3-4a5c-8457-e8cf4cf42e6e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{0, 1}"
            ]
          },
          "execution_count": 38,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Z2={0,1}\n",
        "Z3={0,1,2}\n",
        "Z2.intersection(Z3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00196-fd5bfdda-5af2-4faf-bd13-bca4b6bbde32",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 16,
        "execution_start": 1628264138245,
        "source_hash": "ce4b41e8",
        "tags": [],
        "id": "ixUjxa7KXagK",
        "outputId": "487e6acf-140e-47da-f84a-8a5c3b7c4671"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{0, 1, 2}"
            ]
          },
          "execution_count": 39,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Z2.union(Z3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00197-6ba20ea9-c862-4182-886e-4a76eeb25a27",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 15,
        "execution_start": 1628264144436,
        "source_hash": "fef88faf",
        "tags": [],
        "id": "TD_CnWUlXagK",
        "outputId": "9e0fe386-8628-4316-d6ca-f7ae09fe595a"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 40,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Z2.issubset(Z3)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00198-43b77bb5-1850-4a49-b697-3968c1701891",
        "deepnote_cell_type": "markdown",
        "tags": [],
        "id": "H5MrVs-EXagL"
      },
      "source": [
        "The elements of the set must be unique and sorted"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00199-43c0fa17-d593-4a45-a5f8-d8677893d730",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 19,
        "execution_start": 1628264176162,
        "source_hash": "8a290927",
        "tags": [],
        "id": "AtJRka4rXagL",
        "outputId": "7f9b7435-5e61-4498-f2c8-da9e892c5c4b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{-2, 1, 2, 4}"
            ]
          },
          "execution_count": 41,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "U={1,2,2,2,4,4,-2}\n",
        "U"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00224-b4f9c550-357a-460a-a61a-e739edb86a3c",
        "deepnote_cell_type": "markdown",
        "tags": [],
        "id": "4vFgpwGQXagL"
      },
      "source": [
        "Aplicación: Obtenga los elementos únicos de una lista"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00224-4fc00209-be18-4234-b674-fad7a3b729a5",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 10,
        "execution_start": 1628264330405,
        "source_hash": "edbb9604",
        "tags": [],
        "id": "J_HYJ7qFXagL",
        "outputId": "9d7c4469-3ba3-43ae-a276-71293747f944"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[1, 3, 4, 6, 7, 9]"
            ]
          },
          "execution_count": 45,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "l=[3,7,1,9,4,6,6]\n",
        "list(set(l))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00193-7e91df8a-eda1-4c27-81f3-31632f1f9d02",
        "deepnote_cell_type": "markdown",
        "id": "oMhSjbqYF_1C"
      },
      "source": [
        "# Conditionals"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00194-ccd82614-c309-4aae-888a-0699cfc1f46f",
        "deepnote_cell_type": "markdown",
        "id": "JRx2uDsXF_1C"
      },
      "source": [
        "## if"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00195-1c81bf06-b638-401d-812d-b79c9171eaa1",
        "deepnote_cell_type": "markdown",
        "id": "lOnnZSRpF_1D"
      },
      "source": [
        "Conditionals are useful when we want to check some condition.\n",
        "The statements `elif` and `else` can be used when more than one condition need to be used, or when there is something to do when some condition is not fulfilled."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00196-034330d1-5b3b-4539-86db-8350e8778936",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 10,
        "execution_start": 1628265146080,
        "id": "RLzAJUYrF_1D",
        "outputId": "3454e51b-5dbf-4470-8192-1005c1d3cbdf",
        "source_hash": "f31783ce"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "True\n"
          ]
        }
      ],
      "source": [
        "x = 10\n",
        "y = 2\n",
        "if x > 5 and y==2:\n",
        "    print( \"True\" )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00197-bd759858-0df5-4352-ab75-f1c10c129b36",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 12,
        "execution_start": 1628265185707,
        "id": "Ec7sFHSmF_1H",
        "outputId": "5e5a77ce-f453-45a1-a3d5-58194cd371ee",
        "source_hash": "a3b20567"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "True 2\n"
          ]
        }
      ],
      "source": [
        "x = 4\n",
        "y = 3\n",
        "if x>5 or y<2:\n",
        "    print( \"True 1\" )\n",
        "elif x==4:\n",
        "    print( \"True 2\" )\n",
        "else:\n",
        "    print( \"False\" )"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00205-8a1bdbef-3870-4272-a37f-797627cd74e5",
        "deepnote_cell_type": "markdown",
        "tags": [],
        "id": "QRKixB-dXagM"
      },
      "source": [
        "# Loops"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00198-ed773f4e-f08e-43d6-970f-7c4e7019a757",
        "deepnote_cell_type": "markdown",
        "id": "RKDoomeWF_1J"
      },
      "source": [
        "## for"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00199-b44658ce-9e0d-4402-adee-82a657d3411f",
        "deepnote_cell_type": "markdown",
        "id": "8MS64bApF_1J"
      },
      "source": [
        "`For` cycles are specially useful when we want to sweep a set of elements with a known size."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00200-6566e5ac-b506-4fb4-a8ed-503ef2f5591b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 104
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 18,
        "execution_start": 1628265210358,
        "id": "BGnKwruIF_1K",
        "outputId": "2f93c5e8-66a6-4e74-f268-523891a23892",
        "source_hash": "183ce532"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "0 0\n",
            "1 1\n",
            "2 4\n",
            "3 9\n",
            "4 16\n"
          ]
        }
      ],
      "source": [
        "for i in range(0,5,1):\n",
        "    print( i, i**2)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00201-848f61f8-1f0f-4b60-ba67-52f8c6c0f914",
        "deepnote_cell_type": "markdown",
        "id": "77PbzyH9EW_J"
      },
      "source": [
        "__Activity__: change print with format"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00202-2c2be090-0f25-4d95-b790-b0f637d79d6f",
        "deepnote_cell_type": "code",
        "id": "CEj1vWu_ElkK"
      },
      "outputs": [],
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00203-fe979c0c-86a7-4d7e-856c-e04e71e11d84",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 13,
        "execution_start": 1628265363274,
        "id": "haLnqdCZF_1N",
        "outputId": "ba064e9c-e8e6-407b-8a9d-b63820f5397e",
        "source_hash": "804b79d9"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "The result is 285\n"
          ]
        }
      ],
      "source": [
        "suma = 0\n",
        "for i in range(10):\n",
        "    suma += i**2 # suma = suma + i**2\n",
        "print ( f\"The result is {suma}\" )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00204-04d50356-3b05-44ab-b8da-c2038d6a5b0d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 104
        },
        "deepnote_cell_type": "code",
        "id": "QmjcgnNbF_1P",
        "outputId": "08564dc9-b4da-4f21-ea97-0de3904aa9b8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Python\n",
            "C\n",
            "C++\n",
            "Ruby\n",
            "Java\n"
          ]
        }
      ],
      "source": [
        "for language in ['Python', 'C', 'C++', 'Ruby', 'Java']:\n",
        "    print ( language )"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00205-5ad00505-214e-479e-a2f8-1466c27b9fad",
        "deepnote_cell_type": "markdown",
        "id": "C48dKFMC40bN"
      },
      "source": [
        "As we see before, `for` can be used to build comprenhension lists"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00206-06d3ac31-79de-4718-9d7f-524115f21017",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "id": "lrkdxlQdF_1R",
        "outputId": "bad56fc0-48f2-4219-8b27-e8f6a2f05be9"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[1, 4, 9, 16, 25, 36, 49, 64, 81]\n"
          ]
        }
      ],
      "source": [
        "serie = [ i**2 for i in range(1,10) ]\n",
        "print( serie )"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00207-40757f14-9255-462c-b874-9aaab23a721d",
        "deepnote_cell_type": "markdown",
        "id": "Vk6CUxqjF_1S"
      },
      "source": [
        "## while"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00208-4de1938d-8c8b-424d-93cc-760a1599630f",
        "deepnote_cell_type": "markdown",
        "id": "kys-BDH-F_1T"
      },
      "source": [
        "`While` cycles are specially useful when we want to sweep a set of elements with an  unknown size."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00209-46a116c6-c95f-4c88-b54b-12323ddf1b8f",
        "deepnote_cell_type": "markdown",
        "id": "6RHtEonMXagO"
      },
      "source": [
        "Before we check the functions `input` and `int` of Python"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00210-7d5f306b-eadb-41c8-a7a5-8620a9911e9c",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 4472,
        "execution_start": 1628265392026,
        "source_hash": "ea774bd8",
        "id": "DYxTvtxGXagO"
      },
      "outputs": [],
      "source": [
        "edad=input('¿What is your age, Jesus?:\\n')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00211-445d9a7e-1813-495e-ac39-78c7ffdb3a06",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 13,
        "execution_start": 1628265412246,
        "source_hash": "99514191",
        "id": "SPYiPVs7XagO",
        "outputId": "637ab1bb-976d-46de-b3d2-d7c528b2fda3"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "33"
            ]
          },
          "execution_count": 54,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "int(edad)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00212-a1f22d10-3b95-4b8b-9346-b872991e56c2",
        "deepnote_cell_type": "markdown",
        "id": "_bCB-6HrXagP"
      },
      "source": [
        "Bonus: some time the input must be hidden"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00213-b115e9d4-16aa-4611-833a-bdbc56c614ea",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 0,
        "execution_start": 1628265423279,
        "source_hash": "60de103a",
        "id": "ywlSuV6cXagP"
      },
      "outputs": [],
      "source": [
        "import getpass"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00214-e953a155-b8d1-4805-8c7d-f12307d109cc",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 8198,
        "execution_start": 1628265432333,
        "source_hash": "3329a22",
        "id": "wiQ8pcX_XagP"
      },
      "outputs": [],
      "source": [
        "c=getpass.getpass('Contraseña')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00215-667d4637-b341-4aeb-bfa6-5490014d13ca",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 28,
        "execution_start": 1628265452887,
        "source_hash": "957caa7e",
        "id": "eAxvGsDnXagP",
        "outputId": "34bfd7a9-43a3-43c4-cc72-8b5d98118315"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "'secreto'"
            ]
          },
          "execution_count": 57,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "c"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00216-d72e43af-8ec6-4ded-b701-72f337954cea",
        "deepnote_cell_type": "markdown",
        "id": "3w9Kl_H0XagP"
      },
      "source": [
        "Now the `while` examples"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00217-eee4cc13-f730-43a2-8649-dc08b7c92874",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 156
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 16758,
        "execution_start": 1628265490576,
        "id": "7n0eZTTGF_1T",
        "outputId": "284cf3c9-294c-4282-f6ee-fb587b5439c4",
        "source_hash": "3a149021"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "You wrote a positive number. Do it again\n",
            "You wrote a positive number. Do it again\n",
            "Thank you!\n"
          ]
        }
      ],
      "source": [
        "#! /usr/bin/python\n",
        "number = int(input(\"Write a negative number: \"))\n",
        "while number > 0:\n",
        "    print(\"You wrote a positive number. Do it again\")\n",
        "    number = int(input(\"Write a negative number: \"))\n",
        "print(\"Thank you!\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00218-3d0f8da9-272b-4f29-8dc4-a879189eabd9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 173
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 3,
        "execution_start": 1628265574287,
        "id": "qB2KXTVwF_1W",
        "outputId": "b81f4c44-2cca-4e23-8cf1-7c7a9fbd7b33",
        "source_hash": "bfa297c2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "0.2752802751365522\n",
            "0.454951670912941\n",
            "0.5693802843954813\n",
            "0.40177621529970386\n",
            "0.5723817621908507\n",
            "0.07290420456928348\n",
            "0.8490188174025372\n",
            "0.7299725403288975\n",
            "0.643209656068515\n",
            "0.489899543622623\n",
            "0.2264889834942161\n",
            "0.20635090393901312\n",
            "0.09683376918376296\n",
            "0.14509871628728777\n",
            "0.016240658000300057\n",
            "0.7959386412781978\n",
            "0.4201817808266113\n",
            "0.461661957674957\n",
            "0.8050501425691475\n",
            "0.35466072752783484\n",
            "0.46678267891050707\n",
            "0.21167232860716456\n",
            "0.4891465944627792\n",
            "0.36677308439573475\n",
            "0.7677369600825966\n",
            "0.16631714193575065\n",
            "0.0017489053343822114\n",
            "0.819215365205134\n",
            "0.9499334082744344\n",
            "The selected number was 0.9499334082744344\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "x = 0\n",
        "while x<0.9:\n",
        "    x = random.random()\n",
        "    print( x )\n",
        "print (\"The selected number was\", x )"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00219-7c989cbb-908a-46ad-948f-2e7ad27c80c1",
        "deepnote_cell_type": "markdown",
        "id": "MpuXWP76PRkT"
      },
      "source": [
        "# Methods and attributes of objects in Python\n",
        "All the objects in `Python`, including the function and variable types discussed here, are enhanced with special functions called _methods_, which are implemented after a point of the name of the variable, in the format:\n",
        "```python\n",
        "variable.method()\n",
        "```\n",
        "Some times, the method can even accept some arguments. \n",
        "\n",
        "The objects have also attributes which describe some property of the object. They do not end up with parenthesis:\n",
        "```python\n",
        "variable.attribute\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00220-5bbd289e-7ad7-4874-b6bc-3be16881cfcd",
        "deepnote_cell_type": "markdown",
        "id": "999oCdgfPZOM"
      },
      "source": [
        "### Methods\n",
        "For example. The method `.keys()` of a variable dictionary allows to obtain the list of keys of the dictionary. For example"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00221-45c8146f-c770-45d5-8eb3-8b192124fe7a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 11,
        "execution_start": 1628265625027,
        "id": "nJZOnhPfPb8b",
        "outputId": "e12624c2-f546-4501-a318-1c2a45a18026",
        "source_hash": "b6ec19fd"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "dict_keys(['Kenia', 'Noruega', 'Finlandia', 'Rusia', 'Rio de Janeiro', 'Japón', 'Colorado', 'Alemania', 'Colombia'])"
            ]
          },
          "execution_count": 61,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "dictionary.keys()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00222-bff0bb8f-70c0-4128-9671-42b03bb292e4",
        "deepnote_cell_type": "markdown",
        "id": "4gvGokFJPejs"
      },
      "source": [
        "And the list of values:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00223-76ea55a3-546d-40a4-83dc-d6d59b51fecd",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 23,
        "execution_start": 1628265634377,
        "id": "KcWbTzfjPiKL",
        "outputId": "66d78276-552e-4efb-bb7e-3433a091de62",
        "source_hash": "296aa203"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "dict_values(['Nairobi', 'Oslo', 'Helsinski', 'Moscú', 'Rio', 'Tokio', 'Denver', 'Berlin', 'Bogotá'])"
            ]
          },
          "execution_count": 62,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "dictionary.values()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00224-9ebc6649-40f0-4730-877f-77db92a215cd",
        "deepnote_cell_type": "markdown",
        "id": "op4UiMHFPkek"
      },
      "source": [
        "For strings we have for example the conversion to lower case"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00225-5dde53e2-d039-4597-9d7d-974a3e815cb7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 0,
        "execution_start": 1628265681193,
        "id": "yMXxDJymPsi7",
        "outputId": "8d517979-7568-442d-ceea-296ad29f10f7",
        "source_hash": "cd9af8b1"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "'juan valdez'"
            ]
          },
          "execution_count": 64,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "s=\"Juan Valdez\"\n",
        "s.lower()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00226-04aecf5a-3a55-4557-aee7-620233fab762",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 14,
        "execution_start": 1628265692276,
        "source_hash": "6a1e684f",
        "id": "F8U0U9oaXagR",
        "outputId": "bd981098-8c15-45f8-e0f8-50ff3949a2fb"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "'Juan Valdez'"
            ]
          },
          "execution_count": 65,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "\"juan valdez\".title()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00227-71f0c11e-b4d8-4ade-ac9b-12db09299a3f",
        "deepnote_cell_type": "code",
        "id": "xYbLxmy3XagS",
        "outputId": "5678107e-b85b-40cd-e774-5709aeb093d3"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "'JUAN VALDEZ'"
            ]
          },
          "execution_count": 178,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "\"juan valdez\".upper()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00228-1201df6f-5487-4fb1-a596-4b1a123eae7f",
        "deepnote_cell_type": "markdown",
        "id": "NaWNpAh8PtAD"
      },
      "source": [
        "### Attributes"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00229-2bc92544-1312-423e-ab22-712683d1e348",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 0,
        "execution_start": 1628265704401,
        "id": "yWVg_HMVP4li",
        "source_hash": "b3c0e02"
      },
      "outputs": [],
      "source": [
        "a=1j"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00230-c21184cd-2172-45ed-9b28-244db6ef4d53",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 16,
        "execution_start": 1628265708612,
        "id": "TZLoLjFKP6gT",
        "outputId": "bfb38dc9-dce8-4816-ff63-f4215ac9d36f",
        "source_hash": "899b6bb5"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "1.0"
            ]
          },
          "execution_count": 67,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "a.imag"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00231-95095040-ece2-48db-a372-8a310f6fc62a",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 14,
        "execution_start": 1628265712855,
        "source_hash": "eb5812a6",
        "id": "q4EdoOVWXagT",
        "outputId": "cbbd0155-45ac-412e-b6ae-de4a4230769d"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0.0"
            ]
          },
          "execution_count": 68,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "a.real"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00232-d9027365-efdb-4ce2-993b-b10a4030bffe",
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 1,
        "execution_start": 1628265724255,
        "id": "4YDuZvgbqQTh",
        "source_hash": "f331e88a"
      },
      "outputs": [],
      "source": [
        "z=3+5j"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00233-e9601ee1-45fd-4eb1-b2d8-fd3cb23fa5f6",
        "deepnote_cell_type": "markdown",
        "id": "bwin2MdGRGI5"
      },
      "source": [
        "with attributes"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00234-39ca7c2d-fd8a-4105-95ad-ec463a38dbb5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 13,
        "execution_start": 1628265725782,
        "id": "vXiWuELxqS-u",
        "outputId": "d53786d9-1421-4e22-b7d3-00629bdb711a",
        "source_hash": "91d63406"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "3.0"
            ]
          },
          "execution_count": 70,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "z.real"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00235-0407aed1-af85-4a4c-9910-a8c1e0a5462b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 15,
        "execution_start": 1628265726560,
        "id": "twft_75iqUXd",
        "outputId": "e6cc0c3d-d882-432d-93c9-cc11edfb59aa",
        "source_hash": "a3b5f781"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "5.0"
            ]
          },
          "execution_count": 71,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "z.imag"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00236-10a55c4e-8019-48c7-836c-d27ad9f2962c",
        "deepnote_cell_type": "markdown",
        "id": "3S4SCByKRInH"
      },
      "source": [
        "and the method:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00237-de90673c-4803-426b-8c12-185c54ad9294",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "deepnote_to_be_reexecuted": false,
        "execution_millis": 10,
        "execution_start": 1628265731069,
        "id": "FtsN8LmERK8_",
        "outputId": "894b51eb-34fd-4fce-c3d6-3ff382a1c25c",
        "source_hash": "a7c71621"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "(3-5j)"
            ]
          },
          "execution_count": 72,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "z.conjugate()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00238-c110becb-a3b2-4f5a-8adf-cf0b68e9e9c4",
        "deepnote_cell_type": "markdown",
        "id": "mqPXQ2THP-Kz"
      },
      "source": [
        "In the notebook, All the methods and attributes of an object can be accessed by using the `<TAB>` key after write down the point:\n",
        "```python\n",
        "variable.<TAB>\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00239-980daca3-f063-4cb8-b9e1-b5a9918208fe",
        "deepnote_cell_type": "code",
        "id": "IKvhvPBEIhb7"
      },
      "outputs": [],
      "source": [
        "z."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00240-095cdf89-d7a1-4e9d-ae28-7f7499718117",
        "deepnote_cell_type": "markdown",
        "id": "iBQGxzuFQCID"
      },
      "source": [
        "__Activity__: Check the methods and attributes of the dictionary `dictonary`. HINT: Check the help for some of them by using a question mark, \"?\", at the end:\n",
        "```\n",
        "variable.method?\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00241-8546677a-b493-4719-a269-af0277736ecb",
        "deepnote_cell_type": "markdown",
        "id": "xJBhkIFf40bz"
      },
      "source": [
        "## Unicode\n",
        "Is an standard to encode characters. In Python 3, around  [120.000 characters](https://stackoverflow.com/a/17043983) can be used to define variables. For example, one right to left arabic variable can be defined as"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00242-a2d5676f-9e67-445a-838c-128e2dc6249e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "deepnote_cell_type": "code",
        "id": "E2GeG8HZ40bz",
        "outputId": "579f4e15-ea31-41aa-d8ca-ae1a3baca18e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Arabic character values is: 2\n"
          ]
        }
      ],
      "source": [
        "ࢶ=2\n",
        "print('Arabic character values is: {}'.format(ࢶ))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00243-997768d1-b304-4300-b5cc-d0cb595f6dc2",
        "deepnote_cell_type": "markdown",
        "id": "sdVB50fe40b0"
      },
      "source": [
        "Spanish example"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00244-b53637d7-91bd-4f03-bc28-8ac9ec50515f",
        "deepnote_cell_type": "code",
        "id": "DznrKWaDjv8W"
      },
      "outputs": [],
      "source": [
        "mamá='Lola'"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00245-b9eb3447-2fb3-47bb-9c5f-8abe85ef4f62",
        "deepnote_cell_type": "markdown",
        "id": "PftXYj-K40b2"
      },
      "source": [
        "In Jupyter lab greek symbols can be accessed by using its LaTeX command follow by the `<TAB>` key. \n",
        "\n",
        "`\\alpha+<TAB>=0.5` could convert on the fly to "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00246-7e355b2b-397d-4174-aa93-2ad6e1981a74",
        "deepnote_cell_type": "code",
        "id": "s-HaoMaN40b2"
      },
      "outputs": [],
      "source": [
        "α=0.5"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00247-82438024-40c5-455b-b423-9f19cdfef009",
        "deepnote_cell_type": "code",
        "id": "-FDXnyJD40b3",
        "outputId": "9cb517f1-cc0b-4ad4-f18b-d52b110329a3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "0.5\n"
          ]
        }
      ],
      "source": [
        "print(α)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00248-7cd60ec8-729d-4af2-8a95-600cc07c3785",
        "deepnote_cell_type": "markdown",
        "id": "7NgyW2Sv40b4"
      },
      "source": [
        "Alternatively yuo can copy the character from some list of unicode symbols, like [this one](https://en.wikipedia.org/wiki/List_of_Unicode_characters#Greek_and_Coptic).\n",
        "\n",
        "__Activity__: Define a Greek variable by using a symbol from the previous list"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8KJGU_azXagW"
      },
      "source": [
        "## Stop exection\n",
        "Stop the program if a condition is not satisfied\n",
        "\n",
        "See: https://realpython.com/python-exceptions/"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00249-85eb53c1-6765-4d62-b074-52bf7af37cab",
        "deepnote_cell_type": "code",
        "id": "Ym0NpCWxKJQB",
        "outputId": "b80c6665-3282-47b3-f23f-007281317c70"
      },
      "outputs": [
        {
          "ename": "Exception",
          "evalue": "x should not exceed 5. The value of x was: 6",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mException\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_30232/2136376697.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mx\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m6\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mx\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m5\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m     \u001b[0;32mraise\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'x should not exceed 5. The value of x was: {}'\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf'codo continues here: {x}<=5'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mException\u001b[0m: x should not exceed 5. The value of x was: 6"
          ]
        }
      ],
      "source": [
        "x = 6\n",
        "if x > 5:\n",
        "    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))\n",
        "\n",
        "print(f'codo continues here: {x}<=5')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00250-278fdad9-ce65-4221-89fb-ade632e04fc3",
        "deepnote_cell_type": "markdown",
        "id": "9MgMakz7jhml"
      },
      "source": [
        "## Final remarks\n",
        "Make your google Python questions in English and check specially the https://stackoverflow.com/ results.\n",
        "\n",
        "__Activity__: Make some Python query in Google and paste the example code below"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00251-7f042922-3e62-4e71-809f-26bc971c1edf",
        "deepnote_cell_type": "code",
        "id": "iEtlCAbZ40b6"
      },
      "outputs": [],
      "source": [
        "input('What was the Google query that you ask?:\\n')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00252-f20faff6-23e0-4933-9348-b6b7a9fbe414",
        "deepnote_cell_type": "code",
        "id": "DZG2Mb8cbHur"
      },
      "outputs": [],
      "source": [
        "β"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00253-27ad1dc9-d0c4-4c8c-9d2b-2c6a404419d3",
        "deepnote_cell_type": "markdown",
        "id": "_fIw7E_a40b7"
      },
      "source": [
        "Sample code:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00254-2ad05951-d3e8-4ca1-a8f1-ab7cd8194550",
        "deepnote_cell_type": "markdown",
        "id": "3ewNZO8WXagX"
      },
      "source": [
        "## Parallel\n",
        "```python\n",
        "foo(x) → delayed(foo)(x)\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "cell_id": "00255-3b6d8bea-7285-4f2c-b484-4fe59b794fc3",
        "deepnote_cell_type": "code",
        "id": "_3kGOxElXagX",
        "outputId": "c8c82624-8eb5-4ba0-fd8a-81ed37985c66"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]"
            ]
          },
          "execution_count": 160,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        ">>> from joblib import Parallel, delayed\n",
        ">>> from math import sqrt\n",
        ">>> Parallel(n_jobs=8)(delayed(sqrt)(i**2) for i in range(10))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "cell_id": "00256-175d7309-fc80-45cb-9898-fa05efbdeb88",
        "deepnote_cell_type": "markdown",
        "id": "P9VerMZ7XagX"
      },
      "source": [
        "See also: https://docs.python.org/3/library/multiprocessing.html"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "created_in_deepnote_cell": true,
        "deepnote_cell_type": "markdown",
        "tags": [],
        "id": "dpfmtzygXagY"
      },
      "source": [
        "<a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=f91b818d-f536-4b8f-81de-61752e0979b7' target=\"_blank\">\n",
        "<img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>\n",
        "Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>"
      ]
    }
  ],
  "metadata": {
    "celltoolbar": "Slideshow",
    "colab": {
      "name": "overview-python.ipynb",
      "provenance": []
    },
    "deepnote": {},
    "deepnote_execution_queue": [],
    "deepnote_notebook_id": "c3dc6802-2cbf-4afc-85fa-c70d967f9c3a",
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.2"
    },
    "toc": {
      "colors": {
        "hover_highlight": "#DAA520",
        "running_highlight": "#FF0000",
        "selected_highlight": "#FFD700"
      },
      "moveMenuLeft": true,
      "nav_menu": {
        "height": "390px",
        "width": "252px"
      },
      "navigate_menu": true,
      "number_sections": true,
      "sideBar": true,
      "threshold": 4,
      "toc_cell": false,
      "toc_section_display": "block",
      "toc_window_display": false
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
