{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import unittest\n",
    "from clasificadores.Clasificador_Avestruz import Clasificador_Avestruz as es_Avestruz\n",
    "\n",
    "\n",
    "class TestAvestruz(unittest.TestCase):\n",
    "    \n",
    "    def test_Avestruz(self):\n",
    "        self.assertFalse(es_Avestruz.evaluar('../test_img/albaca.jpg'))\n",
    "        self.assertTrue(es_Avestruz.evaluar('../test_img/Ostrich.jpg'))\n",
    "        \n",
    "if __name__ == '__main__':\n",
    "    unittest.main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
