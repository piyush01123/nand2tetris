
/*
Compile this as javac assembler.java
Then run as java Assembler Xxx.asm Xxx.hack
*/

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

class Parser{
  int c;
  public void Parser (FileReader fr){
    try{
      c=fr.read();      
    } catch (IOException e){}
  }
  public String nextLine(){
    try{
      String line = "";
      while((char)c != '\n'){
        line += (char)c;
        c++;
        return line;
      }
    } catch (IOException e){}
      return "";
  }
  boolean EndOfFile(){
    return c==-1;
  }
}


class Code{
  public void Parser(){

  }
}

class SymbolTable{
  public void SymbolTable(){

  }
}


class Assembler{
  public static void main(String[] args) {
    try {
      String asm_filepath = args[0]; // assembly language code(r)
      String mac_filepath = args[1]; //machine language code(w)
      FileReader asm_file = new FileReader(asm_filepath);
      FileWriter mac_file = new FileWriter(mac_filepath);

      // int c;
      //  while ((c = asm_file.read()) != -1) {
      //     mac_file.write((char)c);
      //  }
      //  asm_file.close();
      //  mac_file.close();
      Parser p = Parser(asm_file);
      System.out.println(p.nextLine());

    } catch (IOException e) {
      System.out.println("File not found issue");
    }
    // System.out.println(args.length);
    // for (int i=0;i<args.length;i++) {
    //   System.out.println(args[i]);
    // }
    return;
  }
}
