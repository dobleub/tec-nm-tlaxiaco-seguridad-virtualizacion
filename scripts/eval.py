#!bash/bin/python3

"""
This script is used to evaluate the model on the test set.
"""

import os
import sys

def is_number(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

def main(baseFile, evalFile):
  baseFileContentStr = open(baseFile, "r").read()
  evalFileContentStr = open(evalFile, "r").read()

  baseFileContent = baseFileContentStr.split("\n")
  evalFileContent = evalFileContentStr.split("\n")

  nameEvalFile = evalFileContent[2]
  print(f"Comparing {baseFile} from {nameEvalFile}")
  nQuestions = 0
  score = 0
  for i in range(len(baseFileContent)):
    questionNumberBase = baseFileContent[i].split(" ")[0].replace(".", "")

    for j in range(len(evalFileContent)):
      questionNumberEval = evalFileContent[j].split(" ")[0].replace(".", "")

      if is_number(questionNumberBase) and is_number(questionNumberEval):
        # Found the same question
        questionBase = str.join(" ", baseFileContent[i].split(" ")[1:])
        questionEval = str.join(" ", evalFileContent[j].split(" ")[1:])
        if questionBase == questionEval and questionBase != "":
          # Found the same answer list
          answerBase = [x.replace("**", "") for x in baseFileContent[i + 2:i + 6]]
          answerEval = [x.replace("**", "") for x in evalFileContent[j + 2:j + 6]]

          print(f"Question %s %s" % (questionNumberEval, questionBase))
          isCorrectList = []
          nQuestions += 1
          for k in range(len(answerBase)):
            answerBaseNumber, answerBaseType = answerBase[k].split(") ")
            isBaseChecked = False if "[ ]" in answerBaseNumber else True
            answerBaseNumber = answerBaseNumber[-1]
            for l in range(len(answerEval)):
              answerEvalNumber, answerEvalType = answerEval[l].split(") ")
              isEvalChecked = False if "[ ]" in answerEvalNumber else True
              answerEvalNumber = answerEvalNumber[-1]
              if answerBaseNumber == answerEvalNumber:
                checked = ("✅" if isEvalChecked == isBaseChecked else "❌") if isBaseChecked else ("❌" if isEvalChecked else "")
                if checked != "":
                  isCorrectList.append(checked)
                print(f"  Answer %s: %s %s" % ("*"+answerEvalNumber if isBaseChecked else " "+answerEvalNumber, answerBaseType, checked))
          
          asnwerIsCorrect = True if len(isCorrectList) > 0 and "❌" not in isCorrectList else False
          score += 1 if asnwerIsCorrect else 0

          print(f"Respuesta " + ("correcta" if asnwerIsCorrect else "incorrecta"))
          print("")
  
  # Calculate the score
  finalScore = 100 * score / nQuestions
  print(f"Name: {nameEvalFile}")
  print(f"Score: {score} of {nQuestions} questions = {finalScore}/100")

  return "Done"

if __name__ == "__main__":
  baseFile = sys.argv[1]
  evalFile = sys.argv[2]

  compareFileContent = main(baseFile, evalFile)
  print(compareFileContent)
