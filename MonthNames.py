{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5b078b3e-01cf-44d8-b618-59b9253e2d50",
   "metadata": {},
   "source": [
    "## program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "c1c6d2c8-9458-4297-b5e0-3b272e68eb80",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the month (1:12): 01\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Month 1 is January\n"
     ]
    }
   ],
   "source": [
    "# define months\n",
    "months = [\"January\", \"February\", \"March\", \"April\", \"May\", \"June\", \"July\", \"August\", \"September\", \"October\", \"November\", \"December\"]\n",
    "\n",
    "# Input\n",
    "month_number= int(input(\"Enter the month (1:12):\"))\n",
    "\n",
    "\n",
    "if 1 <= month_number <= 12:\n",
    "    # Printing the corresponding month\n",
    "     print(f\"Month {month_number} is {months[month_number - 1]}\")\n",
    "else:\n",
    "    \n",
    "    print(\"Invalid Month\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb2386e9-a757-459c-9aa4-fce934e7b116",
   "metadata": {},
   "source": [
    "## calculate the ticket price based on the age provided by the user"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "2040c33f-13e5-46f8-880b-48618335f66d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your age:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your ticket costs £6.00\n"
     ]
    }
   ],
   "source": [
    "# fULL cHARGE OF A ticket is 6 pund\n",
    "# Half price for age below 16\n",
    "# one-third of the price for people who are 60 years old or more.\n",
    "\n",
    "age = int(input(\"Enter your age: \"))\n",
    "\n",
    "full_price = 6\n",
    "if age < 16:\n",
    "    ticket_price = full_price / 2 # halfprice for <16\n",
    "elif age >= 60:\n",
    "    ticket_price = full_price / 3 # for age 60 and above\n",
    "else :\n",
    "    ticket_price = full_price\n",
    "\n",
    "\n",
    "print(f\"Your ticket costs £{ticket_price:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ab74aec-4df4-4ec5-b6e7-ef2b324ad76e",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
