class Skool:
    def __init__(self,name,raspisanie_urokov,name_utitelei,):
        self.Name = name
        self.Raspisanie_urokov = raspisanie_urokov
        self.Name_utitelei = name_utitelei
grades = [5,4,2,4,5,5,2,2,2,3,3,4,4,4,4,4,5,5,5,5,5,]

 AvverageGrade
 grades: list[int] = [5,4,2,4,5,5,2,2,2,3,3,4,4,4,4,4,5,5,5,5,5,]
 count = len(grades)
 for grade in grades:
     sum += grade
     result = round(sum / count)
avv = Avverage(grades)
print(avv)