from DALMember import DALMember

if __name__ == "__main__":
    login= DALMember()
    rows = login. QueryMember(49906106)
    if rows !=0:
        print 'Successful'



