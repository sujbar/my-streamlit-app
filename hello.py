{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bb64e688",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n",
      "  Obtaining dependency information for streamlit from https://files.pythonhosted.org/packages/62/b1/44bd5f0eb1a6d9fa045db1e8bca77dc6751c12f7dacebf820ee708ea5acc/streamlit-1.47.0-py3-none-any.whl.metadata\n",
      "  Downloading streamlit-1.47.0-py3-none-any.whl.metadata (9.0 kB)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Collecting blinker<2,>=1.5.0 (from streamlit)\n",
      "  Obtaining dependency information for blinker<2,>=1.5.0 from https://files.pythonhosted.org/packages/10/cb/f2ad4230dc2eb1a74edf38f1a38b9b52277f75bef262d8908e60d957e13c/blinker-1.9.0-py3-none-any.whl.metadata\n",
      "  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)\n",
      "Collecting cachetools<7,>=4.0 (from streamlit)\n",
      "  Obtaining dependency information for cachetools<7,>=4.0 from https://files.pythonhosted.org/packages/00/f0/2ef431fe4141f5e334759d73e81120492b23b2824336883a91ac04ba710b/cachetools-6.1.0-py3-none-any.whl.metadata\n",
      "  Downloading cachetools-6.1.0-py3-none-any.whl.metadata (5.4 kB)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: numpy<3,>=1.23 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (1.24.3)\n",
      "Requirement already satisfied: packaging<26,>=20 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (24.2)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (2.0.3)\n",
      "Requirement already satisfied: pillow<12,>=7.1.0 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (10.0.1)\n",
      "Collecting protobuf<7,>=3.20 (from streamlit)\n",
      "  Obtaining dependency information for protobuf<7,>=3.20 from https://files.pythonhosted.org/packages/44/3a/b15c4347dd4bf3a1b0ee882f384623e2063bb5cf9fa9d57990a4f7df2fb6/protobuf-6.31.1-cp310-abi3-win_amd64.whl.metadata\n",
      "  Downloading protobuf-6.31.1-cp310-abi3-win_amd64.whl.metadata (593 bytes)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (19.0.1)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
      "  Obtaining dependency information for gitpython!=3.1.19,<4,>=3.0.7 from https://files.pythonhosted.org/packages/01/61/d4b89fec821f72385526e1b9d9a3a0385dda4a72b206d28049e2c7cd39b8/gitpython-3.1.45-py3-none-any.whl.metadata\n",
      "  Downloading gitpython-3.1.45-py3-none-any.whl.metadata (13 kB)\n",
      "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
      "  Obtaining dependency information for pydeck<1,>=0.8.0b4 from https://files.pythonhosted.org/packages/ab/4c/b888e6cf58bd9db9c93f40d1c6be8283ff49d88919231afe93a6bcf61626/pydeck-0.9.1-py2.py3-none-any.whl.metadata\n",
      "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
      "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from streamlit) (6.3.2)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (1.35.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
      "  Obtaining dependency information for gitdb<5,>=4.0.1 from https://files.pythonhosted.org/packages/a0/61/5c78b91c3143ed5c14207f463aecfc8f9dbb5092fb2869baf37c273b2705/gitdb-4.0.12-py3-none-any.whl.metadata\n",
      "  Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (1.26.16)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
      "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
      "  Obtaining dependency information for smmap<6,>=3.0.1 from https://files.pythonhosted.org/packages/04/be/d09147ad1ec7934636ad912901c5fd7667e1c858e19d355237db0d0cd5e4/smmap-5.0.2-py3-none-any.whl.metadata\n",
      "  Downloading smmap-5.0.2-py3-none-any.whl.metadata (4.3 kB)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (22.1.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\sujba\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n",
      "Downloading streamlit-1.47.0-py3-none-any.whl (9.9 MB)\n",
      "   ---------------------------------------- 0.0/9.9 MB ? eta -:--:--\n",
      "   ---------------------------------------- 0.0/9.9 MB 653.6 kB/s eta 0:00:16\n",
      "    --------------------------------------- 0.2/9.9 MB 1.9 MB/s eta 0:00:06\n",
      "   - -------------------------------------- 0.4/9.9 MB 2.6 MB/s eta 0:00:04\n",
      "   -- ------------------------------------- 0.6/9.9 MB 3.4 MB/s eta 0:00:03\n",
      "   --- ------------------------------------ 1.0/9.9 MB 4.1 MB/s eta 0:00:03\n",
      "   ----- ---------------------------------- 1.5/9.9 MB 5.2 MB/s eta 0:00:02\n",
      "   ------- -------------------------------- 1.9/9.9 MB 5.8 MB/s eta 0:00:02\n",
      "   --------- ------------------------------ 2.4/9.9 MB 6.3 MB/s eta 0:00:02\n",
      "   ------------ --------------------------- 3.1/9.9 MB 7.2 MB/s eta 0:00:01\n",
      "   -------------- ------------------------- 3.7/9.9 MB 7.8 MB/s eta 0:00:01\n",
      "   ----------------- ---------------------- 4.2/9.9 MB 8.2 MB/s eta 0:00:01\n",
      "   -------------------- ------------------- 5.0/9.9 MB 8.8 MB/s eta 0:00:01\n",
      "   ---------------------- ----------------- 5.7/9.9 MB 9.3 MB/s eta 0:00:01\n",
      "   ------------------------- -------------- 6.4/9.9 MB 9.8 MB/s eta 0:00:01\n",
      "   ----------------------------- ---------- 7.3/9.9 MB 10.1 MB/s eta 0:00:01\n",
      "   --------------------------------- ------ 8.3/9.9 MB 10.9 MB/s eta 0:00:01\n",
      "   ------------------------------------- -- 9.3/9.9 MB 11.4 MB/s eta 0:00:01\n",
      "   ---------------------------------------  9.9/9.9 MB 11.8 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 9.9/9.9 MB 11.0 MB/s eta 0:00:00\n",
      "Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)\n",
      "Downloading cachetools-6.1.0-py3-none-any.whl (11 kB)\n",
      "Downloading gitpython-3.1.45-py3-none-any.whl (208 kB)\n",
      "   ---------------------------------------- 0.0/208.2 kB ? eta -:--:--\n",
      "   --------------------------------------- 208.2/208.2 kB 13.2 MB/s eta 0:00:00\n",
      "Downloading protobuf-6.31.1-cp310-abi3-win_amd64.whl (435 kB)\n",
      "   ---------------------------------------- 0.0/435.3 kB ? eta -:--:--\n",
      "   --------------------------------------- 435.3/435.3 kB 13.7 MB/s eta 0:00:00\n",
      "Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
      "   ---------------------------------------- 0.0/6.9 MB ? eta -:--:--\n",
      "   ----- ---------------------------------- 1.0/6.9 MB 21.6 MB/s eta 0:00:01\n",
      "   ---------- ----------------------------- 1.8/6.9 MB 18.8 MB/s eta 0:00:01\n",
      "   -------------- ------------------------- 2.5/6.9 MB 17.4 MB/s eta 0:00:01\n",
      "   ------------------- -------------------- 3.4/6.9 MB 17.9 MB/s eta 0:00:01\n",
      "   ------------------------- -------------- 4.4/6.9 MB 18.7 MB/s eta 0:00:01\n",
      "   ------------------------------ --------- 5.3/6.9 MB 18.8 MB/s eta 0:00:01\n",
      "   ------------------------------------- -- 6.5/6.9 MB 19.9 MB/s eta 0:00:01\n",
      "   ---------------------------------------  6.9/6.9 MB 19.1 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 6.9/6.9 MB 16.9 MB/s eta 0:00:00\n",
      "Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)\n",
      "   ---------------------------------------- 0.0/62.8 kB ? eta -:--:--\n",
      "   ---------------------------------------- 62.8/62.8 kB ? eta 0:00:00\n",
      "Downloading smmap-5.0.2-py3-none-any.whl (24 kB)\n",
      "Installing collected packages: smmap, protobuf, cachetools, blinker, pydeck, gitdb, gitpython, streamlit\n",
      "Successfully installed blinker-1.9.0 cachetools-6.1.0 gitdb-4.0.12 gitpython-3.1.45 protobuf-6.31.1 pydeck-0.9.1 smmap-5.0.2 streamlit-1.47.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "12639621",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-07-24 14:57:33.255 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-24 14:57:33.761 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\sujba\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-07-24 14:57:33.762 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-24 14:57:33.764 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-24 14:57:33.767 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-24 14:57:33.768 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-24 14:57:33.769 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "st.title(\"My First Streamlit App\")\n",
    "st.write(\"Hello from Docker!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0175fdee",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3031887691.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[5], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    streamlit hello\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit hello\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c58d9e33",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (4284796380.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[6], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    streamlit run hello.py\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a933451",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
