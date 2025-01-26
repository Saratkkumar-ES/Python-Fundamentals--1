{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "76d3a574-9923-4894-b157-63191848ca3e",
   "metadata": {},
   "source": [
    "## BMI Calculator\n",
    "BMI= weight(kg)/height2(m2)\n",
    "# BMI range - kg/m2   Category\n",
    "# Below -18.5         Underweight\n",
    "# 18.5 -24.9          Normal\n",
    "# 25 -29.9            Overweight\n",
    "# 30 & Above          Obese\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "ced63214-de8f-4465-b36b-26abfe0248d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your weight in (Kg): 68\n",
      "Enter your height in (m): 1.72\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your BMI is: 22.99\n",
      "You are in the \"Normal\" range.\n"
     ]
    }
   ],
   "source": [
    "# Inputing Weight and Height\n",
    "\n",
    "weight = float(input(\"Enter your weight in (Kg):\"))\n",
    "height = float(input(\"Enter your height in (m):\"))\n",
    "\n",
    "        # BMI\n",
    "bmi = weight /(height** 2)\n",
    "# bmi rate range\n",
    "if bmi < 18.5:\n",
    "    category = \"Underweight\"\n",
    "elif 18.5 <= bmi < 24.9:\n",
    "    category = \"Normal\"\n",
    "elif 25 <= bmi < 30:\n",
    "    category = \"OverWeight\"\n",
    "else:\n",
    "    category = \"Obese\"\n",
    "    \n",
    "# Print bmi and category\n",
    "\n",
    "print(f\"Your BMI is: {bmi:.2f}\")\n",
    "print(f\"You are in the \\\"{category}\\\" range.\")"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

