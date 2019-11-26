difusion.png : ej30.dat ej30.py
	python ej30.py
    
ej30.dat : ej30.x
	./ej30.x > ej30.dat

ej30.x : ej30.cpp
	c++ ej30.cpp -o ej30.x

clean:
	rm -rf ej30.x ej30.dat difusion.png
