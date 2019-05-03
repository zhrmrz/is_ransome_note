class Sol:
    def is_ransome_note(self,s,t):
        if s not in t :
            return False
        return True


if __name__ == '__main__':
    p1=Sol()
    print(p1.is_ransome_note('aa','aab'))
