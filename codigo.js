let string s;
s = 'hello world \n \'hola\'\' mundo \\\\\\comentario'
function number FactorialRecursivo (number n)
{
	if (n == 0)	return 1;
	return n * FactorialRecursivo (n - 1);
}

let number uno = 1;	// la inicialización es de implementación opcional
let number UNO = uno;

function string salto ()
{
	return 'hello world\n'';
}

function number FactorialDo (number n)
{
	let number factorial = 0 + uno * 1;	// variable local inicializada a uno
	return factorial;	// devuelve el valor entero de la variable factorial
}

function number FactorialWhile ()
{
	let number factorial = 1;	// variables locales: factorial inicializada a 1
	let	number i;				// variables locales: i inicializada a 0 por omisión
	while (i < num)			// num es variable global entera sin declarar
	{
		factorial *= ++i;	// equivale a: i = i + 1; factorial = factorial * i;
	}
	return factorial;
}

function number FactorialFor (number n)
{
	let number i;
	let number factorial = UNO;
	for (i = 1; i <= n; i++)
	{
		factorial *= i;
	}
	return factorial;
}

let number For;
let number Do;
let number While;	// tres variables globales

function imprime (string s, string msg, number f)
{
	alert(s);alert(msg);alert(f);
	alert (salto());	// imprime un salto de línea */
	return;
}

function string cadena (boolean log)
{
	if (!log) {return s;}
}	// fin cadena: función que devuelve una cadena

// Parte del programa principal:
s = 'El factorial ';	// Primera sentencia que se ejecutaría

alert (s);
alert ('\nIntroduce un número');
input (num);

function boolean bisiesto (number a)
{
	return
		(a % 4 == 0 && a % 100 != 0 || a % 400 == 0);	//se tienen en cuenta la precedencia de operadores
} // fin de bisiesto: función lógica

function number dias (number m, number a)
{
	switch (m)

} // fin de dias. Todos los return devuelven un entero y la función es entera

function boolean esFechaCorrecta (number d, number m, number a)
{
	return m>=1 && m<=12 && d>=1 && d <= dias (m, a);
} //fin de esFechaCorrecta

function imprimeSuma (number v, number w)
{
	alert (v + w);
	alert (salto());
} //fin de imprimeSuma

function potencia (number z, number dim)
{
	let number s;	// Oculta a la global
	for (s=0; s < dim; s++)
	{
	}
} // fin de potencia: función que no devuelve nada

function demo ()
{
	let number v1; let number v2; let number v3;
	let number zv; // Variables locales

	alert ('Escriba "tres" números: ');
	input (v1); input (v2); input (v3);

	if (v3 == 0) return;

	if (!((v1 == v2) && (v1 != v3)))	/* NOT ((v1 igual a v2) AND (v1 distinto de v3))  */
	{
		alert ('Escriba su nombre: ');
		let string s;	// Oculta a la s global
		input (s);
		if (v2 < v3)	/* si v2<v3, v0=v2; en otro caso v0=1/v3 */
		{
			let number v0 = v2; // se declara v0 aquí, por lo que se puede utilizar hasta el final de la función
		}
		else
		{
			v0= 1 / v3;
		}
		alert (s);
	}
	s = 'El primer valor era ';
	if (v1 != 0)
	{
		alert (s); alert (v1); alert ('\n');
	}
	else
	{
		alert (s); imprimeSuma (uno, -UNO); alert ('.\n');	// imprime: `El primer valor era 0.\n´
	}

	potencia (v0, 4);
	let number i;
	for (i=1; i <= 10; ++i)	{
		zv+=i;
	}
	potencia (zv, 5);
	imprimeSuma (i, num);
	imprime ('', cadena(true), 666);
}

demo();