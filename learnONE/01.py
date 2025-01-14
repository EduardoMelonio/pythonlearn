{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNz2qj0v4FBQ/biTVfOUOag"
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
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YWMeLVOmAN00",
        "outputId": "5206adf9-7531-4e2a-e5f2-b124efc5c47f"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ],
      "source": [
        "# example of list comprehension\n",
        "\n",
        "[x for x in range(10)]"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Using conditional with list comprehension\n",
        "# return X to each value of X in element, just if X is iqual 5\n",
        "\n",
        "list = [x for x in range(10) if x < 5]"
      ],
      "metadata": {
        "id": "HgtYSFr1AdQs"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}