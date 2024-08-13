from dbconnection import inserttrainee,selectfromtable,inserttrack,delete_from_trainee,delete_from_tracks,updatetrack,updatetrainee
inserttrack(1,"python",25)
print(selectfromtable("trainee"))
print(selectfromtable("tracks"))
