class Techie:
    def __init__(self, first_name, last_name, job_title):
        self.first = first_name
        self.last = last_name
        self.title = job_title
    
    # Create a function to return the Person's first name     
    def get_first(self):
        return self.first
    
    # Create a function to return the Person's last name     
    def get_last(self):
        return self.last
    
    # Create a function to return the Person's profession     
    def get_title(self):
        return self.title

def main():
    # Corrected statement below.
    techie = Techie('Alexis', 'Martinez', 'Web Application Programmer')
    print(f'{techie.get_first()} {techie.get_last()}')
    print(techie.get_title())

if __name__ == '__main__':
    main()
