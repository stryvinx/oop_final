class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\n")


class Education:
    def __init__(self, degree, school, graduation_year):
        self.degree = degree
        self.school = school
        self.graduation_year = graduation_year

    def display_info(self):
        print(f"{self.degree} in {self.school}, Graduated in {self.graduation_year}\n")


class WorkExperience:
    def __init__(self, job_title, company, start_year, end_year=None):
        self.job_title = job_title
        self.company = company
        self.start_year = start_year
        self.end_year = end_year

    def display_info(self):
        if self.end_year:
            print(f"{self.job_title} at {self.company}, {self.start_year}-{self.end_year}\n")
        else:
            print(f"{self.job_title} at {self.company}, {self.start_year}-Present\n")


class DetailedWorkExperience(WorkExperience):
    def __init__(self, job_title, company, start_year, end_year, responsibilities):
        super().__init__(job_title, company, start_year, end_year)
        self.responsibilities = responsibilities

    def display_info(self):
        super().display_info()
        print("Responsibilities:")
        for responsibility in self.responsibilities:
            print(f"- {responsibility}")
        print()


class CV:
    def __init__(self, person, education, work_experiences):
        self.person = person
        self.education = education
        self.work_experiences = work_experiences

    def generate_cv(self):
        print("Curriculum Vitae (CV)\n")
        self.person.display_info()
        print("Education:")
        self.education.display_info()
        print("Work Experience:")
        for work_experience in self.work_experiences:
            work_experience.display_info()


# Kullanıcıdan bilgileri al
name = input("Adınız: ")
age = int(input("Yaşınız: "))
address = input("Adresiniz: ")

degree = input("Eğitim Derecesi: ")
school = input("Okul Adı: ")
graduation_year = int(input("Mezuniyet Yılı: "))

person = Person(name, age, address)
education = Education(degree, school, graduation_year)

work_experiences = []
while True:
    job_title = input("İş Başlığı: ")
    company = input("Şirket Adı: ")
    start_year = int(input("Başlangıç Yılı: "))
    end_year = int(input("Bitiş Yılı (eğer hala devam ediyorsa boş bırakın): "))
    responsibilities = input("Sorumluluklar (virgülle ayırın): ").split(',')

    if responsibilities == ['']:
        responsibilities = []

    if end_year:
        work_experience = WorkExperience(job_title, company, start_year, end_year)
    else:
        work_experience = DetailedWorkExperience(job_title, company, start_year, None, responsibilities)

    work_experiences.append(work_experience)

    add_more = input("Başka bir iş deneyimi eklemek istiyor musunuz? (E/H): ")
    if add_more.upper() != 'E':
        break

# CV oluştur ve göster
cv = CV(person, education, work_experiences)
cv.generate_cv()


import tkinter as tk
from tkinter import ttk

class CVApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CV Oluşturucu")
        self.geometry("600x400")

        # Kişisel Bilgiler Frame
        personal_info_frame = ttk.LabelFrame(self, text="Kişisel Bilgiler")
        personal_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ttk.Label(personal_info_frame, text="Adı Soyadı:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(personal_info_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(personal_info_frame, text="Yaş:").grid(row=1, column=0, sticky="w")
        self.age_entry = ttk.Entry(personal_info_frame, width=5)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(personal_info_frame, text="Adres:").grid(row=2, column=0, sticky="w")
        self.address_entry = ttk.Entry(personal_info_frame, width=30)
        self.address_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Eğitim Bilgileri Frame
        education_frame = ttk.LabelFrame(self, text="Eğitim Bilgileri")
        education_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        ttk.Label(education_frame, text="Derece:").grid(row=0, column=0, sticky="w")
        self.degree_entry = ttk.Entry(education_frame, width=20)
        self.degree_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(education_frame, text="Okul Adı:").grid(row=1, column=0, sticky="w")
        self.school_entry = ttk.Entry(education_frame, width=30)
        self.school_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(education_frame, text="Mezuniyet Yılı:").grid(row=2, column=0, sticky="w")
        self.graduation_year_entry = ttk.Entry(education_frame, width=10)
        self.graduation_year_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # İş Deneyimi Frame
        work_experience_frame = ttk.LabelFrame(self, text="İş Deneyimi")
        work_experience_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        ttk.Label(work_experience_frame, text="İş Başlığı:").grid(row=0, column=0, sticky="w")
        self.job_title_entry = ttk.Entry(work_experience_frame, width=20)
        self.job_title_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(work_experience_frame, text="Şirket Adı:").grid(row=1, column=0, sticky="w")
        self.company_entry = ttk.Entry(work_experience_frame, width=30)
        self.company_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(work_experience_frame, text="Başlangıç Yılı:").grid(row=2, column=0, sticky="w")
        self.start_year_entry = ttk.Entry(work_experience_frame, width=10)
        self.start_year_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(work_experience_frame, text="Bitiş Yılı:").grid(row=3, column=0, sticky="w")
        self.end_year_entry = ttk.Entry(work_experience_frame, width=10)
        self.end_year_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(work_experience_frame, text="Sorumluluklar (virgülle ayırın):").grid(row=4, column=0, sticky="w")
        self.responsibilities_entry = ttk.Entry(work_experience_frame, width=30)
        self.responsibilities_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # CV Oluştur Butonu
        generate_cv_button = ttk.Button(self, text="CV Oluştur", command=self.generate_cv)
        generate_cv_button.grid(row=3, column=0, pady=10)

    def generate_cv(self):
        # Kullanıcının girdiği bilgileri al
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        address = self.address_entry.get()

        degree = self.degree_entry.get()
        school = self.school_entry.get()
        graduation_year = int(self.graduation_year_entry.get())

        job_title = self.job_title_entry.get()
        company = self.company_entry.get()
        start_year = int(self.start_year_entry.get())
        end_year = int(self.end_year_entry.get()) if self.end_year_entry.get() else None
        responsibilities = self.responsibilities_entry.get().split(',')

        # Nesneleri oluştur
        person = Person(name, age, address)
        education = Education(degree, school, graduation_year)

        work_experiences = []
        if end_year:
            work_experience = WorkExperience(job_title, company, start_year, end_year)
        else:
            work_experience = DetailedWorkExperience(job_title, company, start_year, None, responsibilities)

        work_experiences.append(work_experience)

        # CV oluştur ve göster
        cv = CV(person, education, work_experiences)
        cv.generate_cv()

if __name__ == "__main__":
    app = CVApplication()
    app.mainloop()
