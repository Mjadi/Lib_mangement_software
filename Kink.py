# Creating the class of this management 

class Library:

    # Getting the info of the library
    def details(self, B_name, location, p_Num):
        self.B_name = B_name
        self.location = location
        self.p_Num = p_Num

    # Making the b_info section
    def b_Info(self, Jounra, max_Time, b_Quants=300):
        self.Jounra = Jounra
        self.max_Time = int(max_Time)
        self.b_Quants = int(b_Quants)

# li algo = float, port = int(85), ui = yort sinch, gui(sinch_uojk"85*58") dpkg: "force_Stop"
# ft.port_Val(ry.Val) n_Quart(Val.port), dpkg(Val.li_algo)

    # Showing the b_On details
    def get_B_Details(self):
        print(f'The Name of this Buiss. is {self.B_name}, located in {self.location}, c_Number is {self.p_Num}')

    # Making the m_B function.
    def u_Bo(self, b_N, t_L):
        self.b_N = b_N
        self.t_L = t_L
        
        if self.t_L>self.max_Time:
            print(f'Sorry! but the max time lent is {self.max_Time}.Please try again later')
        
        elif self.t_L<=self.max_Time and self.b_Quants>0:
            self.b_Quants-=1
            print('Thanks for your Issue!')
            print(f'Your borrwed product name is {self.b_N} and time lent is {self.t_L}')
            print(f'Please collect your product from {self.location}')
            print("Do not forget to return it on time!")

    # Getting the user details
    def u_Info(self, name, address, p_Number):
        self.name = name
        self.address = address
        self.p_Number = p_Number
        with open('data_Base.txt', 'a')as f:
            f.writelines((f'The name of the user is {self.name}, his/her address is {self.address}, their phone number is {self.p_Number}\n'))

    # Giving the user details about products and borrow function

    def show_P_Details(self):
        print(f'''The Jounra found is {self.Jounra}, max time lent is {self.max_Time} days, products left is {self.b_Quants}''')

    # Showing the user details
    def show_U_Details(self):
        k_7=int(input('Enter the password\n'))
        password=9091
        if k_7==password:
            with open('data_Base.txt')as l:
                print(l.read())

        elif k_7!=password:
            print('The Password entered by you does not match our database!')

if __name__=='__main__':

    K = Library()

    K.details('Lincon_hub', 'Near secter-7, East_California', '2541698745')
    K.b_Info('NCERT', 15)

    while(True):


        f_2 = input('Enter your request\n')
        if f_2=='Enter Library':
            print('Welcome to our library! Please enter your details.')
            print('We have all variety and releases of NCERT Books$')
            print('If you are an old user enter "Yes", else type "No"')
            f_3 = input("Are you an old user?\n")
            if f_3=='No':

                    L_6 = input('Enter your name: ')
                    L_7 = input('Enter your address\n')
                    L_8 = input('Enter your phone_Num\n')
                    K.u_Info(L_6, L_7, L_8)

                    while(True):
                        p2 = input('How can we help you: ')

                        if p2=='Lib details':
                                    K.get_B_Details()

                        elif p2=='Product_details':
                                    K.show_P_Details()

                        elif p2=='Issue_Bk':
                                    J1 = input('Enter the Book_name: ')
                                    J2 = int(input('For how much time you want to Issue(in days)\n'))
                                    K.u_Bo(J1, J2)
                        elif p2=='q':
                            break

            elif f_3=='Yes':
                k_23 = input('Please enter your username: ')
                with open('data_Base.txt')as n:
                    w_3 = n.read()
                    if k_23 in w_3:
                        while(True):
                            p2 = input('How can we help you: ')

                            if p2=='Lib details':
                                        K.get_B_Details()

                            elif p2=='Product_details':
                                        K.show_P_Details()

                            elif p2=='Issue_Bk':
                                        J1 = input('Enter the Book_name: ')
                                        J2 = int(input('For how much time you want to Issue(in days)\n'))
                                        K.u_Bo(J1, J2)
                            elif p2=='q':
                                break

                    elif k_23 not in w_3:
                        print('Your not an old user! Please sign in.')

        elif f_2=='get user details':
            K.show_U_Details()

        elif f_2=='quit':
            break




