import java.util.Scanner;
import java.util.LinkedList;
public class Main{
  /*
  Método que convierte una cadena de texto a una lista.
  @param cadena, cadena de texto con números y símbbolos de + y *.
  @return lista que separa la cadena en operandos y operadores en notación infija.
  */
  public static LinkedList<String> parser(String cadena){
    LinkedList<String> cola = new LinkedList<>();
    char[] s = cadena.toCharArray();
    String numeros = "";
    for (int i=0; i<s.length; i++){
      if(!(s[i] == '+') && !(s[i]== '*')){
        numeros+= s[i];
        if (i == s.length-1){
          cola.add(numeros);
        }
      } else{
        cola.add(numeros);
        String operacion = Character.toString(s[i]);
        cola.add(operacion);
        numeros = "";
      }
    }
    return cola;
  }

  public static LinkedList<String> producto(LinkedList<String> lista){
    LinkedList<String> cola = new LinkedList<>();
    String salida = "";
    while(!lista.isEmpty()){
      String objeto = lista.pop();
      if (!(objeto.equals("+") || objeto.equals("*"))){
        cola.add(objeto);
      } else
        if(objeto.equals("*")){
          String operando1 = cola.pollLast();
          String operando2 = lista.pop();
          salida = String.valueOf(Integer.parseInt(operando1) * Integer.parseInt(operando2));
          cola.add(salida);
          salida = "";
        } else
          cola.add(objeto);
    }
    return cola;
  }

  public static int suma(LinkedList<String> lista){
    int resultado = 0;
    while(!lista.isEmpty()){
      String operando = lista.pop();
      if (!operando.equals("+")){
        resultado +=Integer.parseInt(operando);
      }
    }
    return resultado;
  }

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String cadena = scan.nextLine();
    LinkedList<String> p = parser(cadena);
    LinkedList<String> m = producto(p);
    int resultado = suma(m);
    System.out.println(resultado);
  }

}
