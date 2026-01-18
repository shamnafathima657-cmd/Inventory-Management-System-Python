{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ba0fff60-42a6-418f-8d90-f831dd3742f6",
   "metadata": {},
   "source": [
    "## inventory management system"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a14babb9-d66f-40d0-8b29-afb9e0fd8ef0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\\_______inventory management_______\n",
      "1.add product\n",
      "2.view product\n",
      "3.update quantity\n",
      "4.remove product\n",
      "5.exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "select a number between 1 to 5: 1\n",
      "enter the productid number: 101\n",
      "enter the product name: pen\n",
      "enter the price of product: 5\n",
      "enter the quantity of the product: 10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pen added successfully\n",
      "\\_______inventory management_______\n",
      "1.add product\n",
      "2.view product\n",
      "3.update quantity\n",
      "4.remove product\n",
      "5.exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "select a number between 1 to 5: 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "-------product list-------\n",
      "ID:101\n",
      "Name:pen\n",
      "Price:5.0\n",
      "Quantity:10\n",
      "--------------------------\n",
      "\\_______inventory management_______\n",
      "1.add product\n",
      "2.view product\n",
      "3.update quantity\n",
      "4.remove product\n",
      "5.exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "select a number between 1 to 5: 3\n",
      "Enter Product ID:  101\n",
      "Enter new quantity:  15\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quantity updated!\n",
      "\\_______inventory management_______\n",
      "1.add product\n",
      "2.view product\n",
      "3.update quantity\n",
      "4.remove product\n",
      "5.exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "select a number between 1 to 5: 4\n",
      "enter product id to delete: 101\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pendeleted successfully\n",
      "\\_______inventory management_______\n",
      "1.add product\n",
      "2.view product\n",
      "3.update quantity\n",
      "4.remove product\n",
      "5.exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "select a number between 1 to 5: 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "exiting.. \n"
     ]
    }
   ],
   "source": [
    "\n",
    "inventory={}\n",
    "\n",
    "while True:\n",
    "    print(\"\\_______inventory management_______\")\n",
    "    print(\"1.add product\")\n",
    "    print(\"2.view product\") \n",
    "    print(\"3.update quantity\")\n",
    "    print(\"4.remove product\")\n",
    "    print(\"5.exit\")\n",
    "    choose=input(\"select a number between 1 to 5:\")\n",
    "    \n",
    "    # add product\n",
    "    if choose == '1':\n",
    "        productid=int(input(\"enter the productid number:\"))\n",
    "        if productid in inventory:\n",
    "                print(\"product already exits\")\n",
    "        else:\n",
    "            name=input(\"enter the product name:\")\n",
    "            price=float(input(\"enter the price of product:\"))\n",
    "            quantity=int(input(\"enter the quantity of the product:\"))\n",
    "            inventory[productid]={\"name\":name,\"price\":price,\"quantity\":quantity}\n",
    "            print(f\"{name} added successfully\")\n",
    "\n",
    "      # view products  \n",
    "    elif choose == '2':\n",
    "        if not inventory:\n",
    "            print(\"no products available\")\n",
    "        else:\n",
    "            print(\"\\n-------product list-------\")\n",
    "            for productid,details in inventory.items():\n",
    "                print(f\"ID:{productid}\")\n",
    "                print(f\"Name:{details['name']}\")\n",
    "                print(f\"Price:{details['price']}\")\n",
    "                print(f\"Quantity:{details['quantity']}\")\n",
    "                print(\"--------------------------\")\n",
    "    # update quantity\n",
    "    elif choose=='3':\n",
    "        productid = int(input(\"Enter Product ID: \"))\n",
    "        if productid in inventory:\n",
    "            quantity = int(input(\"Enter new quantity: \"))\n",
    "            inventory[productid][\"quantity\"] = quantity\n",
    "            print(\"Quantity updated!\")\n",
    "        else:\n",
    "            print(\"Product not found.\")\n",
    "        \n",
    "    #delete product\n",
    "    elif choose=='4':\n",
    "        productid=int(input(\"enter product id to delete:\"))\n",
    "        if productid in inventory:\n",
    "            deleteproduct=inventory.pop(productid)\n",
    "            print(f\"{deleteproduct['name']}deleted successfully\")\n",
    "        else:\n",
    "            print(\"not found \")\n",
    "\n",
    "    #exit\n",
    "    elif choose =='5':\n",
    "        print(\"exiting.. \")\n",
    "        break\n",
    "    else:\n",
    "        print(\"invalid choice.try again\")\n",
    "        \n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
