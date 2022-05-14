class Main :
    def main( args) :
        #adatok inicializálása
        id =  []
        all_data =  []
        calc =  []
        done = 0
        try :
            #adatok beolvasása és tárolása
            while True:
                example = input().split(",")
                if (example[3] == None) :
                    return
                else :
                    all_data.append(example)
        except:
            pass
        wait_time = [0] * (len(all_data))
        i = 0
        while (i < len(all_data)) :
            wait_time[i] = 0
            i += 1
        while (True) :

            #Indítási idő alapján megnézi,
	    #hogy melyik taszk indult már el
            i = 0
            while (i < len(all_data)) :
                if (int(all_data[i][2]) < 1 and 0 < int(all_data[i][3])) :
                    calc.append(all_data[i])
                i += 1
            i = 0
            while (i < len(calc)) :
                j = i + 1
                while (j < len(calc)) :
                    if (int(calc[j][3]) < int(calc[i][3])) :
                        calc[i], calc[j] = calc[j], calc[i]
                    j += 1
                i += 1
            if (len(calc) > 0) :
                i = 0
                while (i < len(all_data)) :
                    if (int(all_data[i][2]) == 0 and int(all_data[i][3]) != 0) :
                        if (all_data[i][0] == calc[0][0]) :
                            all_data[i][3] = str(int(calc[0][3]) - 1)
                        else :
                            wait_time[i] += 1
                    i += 1
            #ID-k sorbarendezése
            if (len(calc) > 0) :
                if (len(id) != 0) :
                    if (id[len(id) - 1] != calc[0][0]) :
                        id.append(calc[0][0])
                else :
                    id.append(calc[0][0])
            calc.clear()
            i = 0
            while (i < len(all_data)) :
                if (int(all_data[i][2]) > 0) :
                    all_data[i][2] = str(int(all_data[i][2]) - 1)
                i += 1
            done = 0
            i = 0

            #kiiratás
            while (i < len(all_data)) :
                if (int(all_data[i][3]) == 0) :
                    done += 1
                    if (done == len(all_data)) :
                        print()
                        j = 0
                        while (j < len(id)) :
                            print(id[j], end ="")
                            j += 1
                        print()
                        k = 0
                        while (k < len(all_data)) :
                            if(k == len(all_data)-1):
                                print(all_data[k][0] + ":" + str(wait_time[k]))
                            else:
                                print(all_data[k][0] + ":" + str(wait_time[k]) + ",", end ="")
                            k += 1
                        return
                i += 1
    

if __name__=="__main__":
    Main.main([])

##Tesztadatok:
##A,1,2,7
##B,1,2,3
##BA
##A:3,B:0
##
##Q,1,5,8
##P,1,7,2
##QPQ
##Q:2,P:0
##
##A,1,0,3
##B,1,0,2
##C,1,3,3
##D,1,4,1
##BADC
##A:2,B:0,C:3,D:1

