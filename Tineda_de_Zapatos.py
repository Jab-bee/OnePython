{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNAMjK58pYBSHpRxuib/orE"
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
      "source": [
        "Eres el gerente de una tienda de zapatos y necesitas controlar tu inventario.\n",
        "\n",
        "Cada vez que vendes un par de zapatos, disminuyes tu inventario. Quieres tener un programa que te permita ingresar la cantidad inicial de pares de zapatos en tu tienda y luego, sucesivamente, te pregunte cuántos pares de zapatos se vendieron. El programa debe continuar preguntando cuántos pares de zapatos se vendieron hasta que el inventario llegue a cero. Finalmente, el programa debe decirte cuántas transacciones (ventas individuales) tuvieron lugar antes de que se acabara el inventario.\n",
        "\n"
      ],
      "metadata": {
        "id": "qyjAGDEHsElW"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AGzXqhT6ow4c",
        "outputId": "2ad8a526-a8b0-4033-cace-4d71e44a471c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese la cantidad inicial de pares de zapatos en la tienda: 200\n",
            "El inventario contiene 200 pares de zapatos.\n"
          ]
        }
      ],
      "source": [
        "# Cantidad inicial de pares de zapatos\n",
        "inventario = int(input(\"Ingrese la cantidad inicial de pares de zapatos en la tienda: \"))\n",
        "transacciones = 0\n",
        "print(f\"El inventario contiene {inventario} pares de zapatos.\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "while inventario > 0:\n",
        "    if inventario < 10:\n",
        "        print(\"Advertencia: el inventario está casi vacío.\")\n",
        "\n",
        "    num_zapatos = int(input(\"¿Cuántos pares de zapatos quiere el cliente? \"))\n",
        "\n",
        "    if num_zapatos > inventario:\n",
        "        print(f\"No hay stock para tanta cantidad. Solo hay {inventario} pares disponibles.\")\n",
        "    else:\n",
        "        inventario -= num_zapatos\n",
        "        transacciones += 1\n",
        "        print(f\"El cliente ha pedido {num_zapatos} pares. Ahora tienes {inventario} pares en el inventario.\")\n",
        "\n",
        "print(f\"Se realizaron un total de {transacciones} transacciones antes de que se acabara el inventario.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MTgZ_JFUtl7a",
        "outputId": "7bb10862-8b34-42d9-8a90-cfc8893c2e00"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "¿Cuántos pares de zapatos quiere el cliente? 5\n",
            "El cliente ha pedido 5 pares. Ahora tienes 164 pares en el inventario.\n",
            "¿Cuántos pares de zapatos quiere el cliente? 6\n",
            "El cliente ha pedido 6 pares. Ahora tienes 158 pares en el inventario.\n",
            "¿Cuántos pares de zapatos quiere el cliente? 30\n",
            "El cliente ha pedido 30 pares. Ahora tienes 128 pares en el inventario.\n",
            "¿Cuántos pares de zapatos quiere el cliente? 25\n",
            "El cliente ha pedido 25 pares. Ahora tienes 103 pares en el inventario.\n",
            "¿Cuántos pares de zapatos quiere el cliente? 32\n",
            "El cliente ha pedido 32 pares. Ahora tienes 71 pares en el inventario.\n",
            "¿Cuántos pares de zapatos quiere el cliente? 14\n",
            "El cliente ha pedido 14 pares. Ahora tienes 57 pares en el inventario.\n",
            "¿Cuántos pares de zapatos quiere el cliente? 5\n",
            "El cliente ha pedido 5 pares. Ahora tienes 52 pares en el inventario.\n",
            "¿Cuántos pares de zapatos quiere el cliente? 89\n",
            "No hay stock para tanta cantidad. Solo hay 52 pares disponibles.\n",
            "¿Cuántos pares de zapatos quiere el cliente? 32\n",
            "El cliente ha pedido 32 pares. Ahora tienes 20 pares en el inventario.\n",
            "¿Cuántos pares de zapatos quiere el cliente? 20\n",
            "El cliente ha pedido 20 pares. Ahora tienes 0 pares en el inventario.\n",
            "Se realizaron un total de 15 transacciones antes de que se acabara el inventario.\n"
          ]
        }
      ]
    }
  ]
}