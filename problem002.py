{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOanutkQk8S9BnHsWOnAMyM",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/violakejrova/Project-Euler/blob/main/problem002.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ugD8tWZstYJn",
        "outputId": "2ac2559b-9d7e-4ca0-9e56-8bbc2cadb3d2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4613732\n"
          ]
        }
      ],
      "source": [
        "def fibonacci(limit):\n",
        "    solve = 0\n",
        "    a, b = 0, 1\n",
        "    while a < limit:\n",
        "        if a % 2 == 0:\n",
        "            solve += a\n",
        "        a, b = b, a + b\n",
        "    return solve\n",
        "\n",
        "print(fibonacci(4000000))"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "S75A8dazudKd"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}