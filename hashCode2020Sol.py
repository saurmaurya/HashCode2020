'''
## Author: Saurabh Ranjan Singh
## Copyright: Copyright 2020, The HashCode2020 Project
## Credits: Saurabh Ranjan Singh
## Maintainer: Saurabh Ranjan Singh
## Email: saurmaurya@gmail.com
## Status: Dev
'''

# Importing the libraries
import os

class HashCode2020:
    '''
    This is a class for getting solution of HashCode2020 practice problem.

    Attributes:
        MAX (list): The list of type str showing maximum number of slices needed.
        fileName (str): The fileName of inputfile.
    '''
    MAX = None
    fileName = ''

    def fileInput(self):
        '''
        The function for getting the input from the file, simply enter the file name when prompt.

        Parameters:
            This function gets no parameter.
        
        Returns:
            Input (list): This function return a list of input of type int.
        '''
        Input = []
        self.fileName = input("Enter the input filename: ")
        if not os.path.exists(self.fileName):
            print('The input file didn\'t exist,',
                  'please re-enter the input filename')
            self.fileInput()
        else:
            print('\nProcessing the input...')
            try:
                inputFile = open(self.fileName, 'r')
            except IOError:
                print('Cannot open the file')
            vars = inputFile.readline().split(' ')
            self.MAX = vars[0]
            Num = vars[1]
            print('-------input of ' + self.fileName + '-------')
            print(self.MAX + ' ' + Num, end='')
            letters = inputFile.readline().split()
            for i in range(0, len(letters)):
                Input.append(int(letters[i]))
                print(letters[i], end=' ')
            print()
            inputFile.close()
        return Input

    def solve(self, Input):
        '''
        The function to solve the input.

        Parameters:
            Input (list): A list of input data of int type

        Returns:
            BestSolution (list): A list of int type of the output
        '''
        BestSolution = []
        score = 0
        i = len(Input) - 1
        test1, test2 = True, True
        while(i > 0 and test1):
            TempBestSolution = []
            j = i
            sum = 0
            while j >= 0 and test2:
                temp = Input[j]
                if sum + temp < int(self.MAX):
                    sum += temp
                    TempBestSolution.append(j)
                elif sum + temp == int(self.MAX):
                    sum += temp
                    TempBestSolution.append(j)
                    test2 = False
                    test1 = False
                j -= 1
            if score < sum:
                score = sum
                BestSolution = TempBestSolution
            if len(BestSolution) == len(Input):
                test1 = False
            i -= 1
        BestSolution.reverse()
        return BestSolution

    def fileOutput(self, Output):
        '''
        The function to generate the output in a file
        
        Parameters:
            Output: A list of the output of str type, to append in the file 
        
        Returns:
            Create a file of Output in the output directory
        '''
        fileName = (self.fileName.partition('/'))[-1]
        print('\n-------output ' + fileName[:-3] + '.out-------')
        try:
            outputFile = open(
                ('output\\' + fileName[0:-3] + '.out'), 'w', encoding='UTF-8')
        except IOError:
            print('Cannot process the output')
        outputFile.write(str(len(Output)) + '\n')
        print(len(Output))
        for i in range(0, len(Output)):
            outputFile.write((str(Output[i])) + ' ')
            print(str(Output[i]), end=' ')
        outputFile.close()


if __name__ == "__main__":
    obj = HashCode2020()
    input = obj.fileInput()
    print(input)

    # Getting the output
    output = obj.solve(input)
    print(output)

    # Creating the output directory if not exist
    if not os.path.exists('output'):
        os.mkdir('output')
    
    # Saving the output in a file to the output directory
    obj.fileOutput(output)

