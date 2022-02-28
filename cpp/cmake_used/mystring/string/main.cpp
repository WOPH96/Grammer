#include <iostream>

class string {
  char *str;
  int len;

 public:
  string(char c,const int n);  // 문자 c 가 n 개 있는 문자열로 정의
  string(const char *s);
  string(const string &s);
  ~string();

  void add_string(const string &s);   // str 뒤에 s 를 붙인다.
  void copy_string(const string &s);  // str 에 s 를 복사한다.
  int strlen();                       // 문자열 길이 리턴
};

string::string(char c,const int n){
    this->str = new char[n+1];
    this->len = n; 
    int i;
    for(i=0; i<n; i++){
        str[i]=c;
    }
    str[i]='\0';
    
    std::cout << str << std::endl;
}

string::string(const char *s){
    this->len = 0;

    while(*s){
        s++;
        len++;
    }

    this->str = new char[len+1];
    s-=len;
    
    for(int i=0; i<len; i++){
        str[i] = s[i];
    }
    str[len]=(char)NULL;
    std::cout << str << std::endl;

}
string::string(const string &s){
    this->len = s.len;
    this->str = new char[len+1];
    for(int i=0; i<len; i++){
        str[i] = s.str[i];
    }
    str[len]=(char)NULL;
    std::cout << str << std::endl;

}
string::~string(){
    std::cout << "소멸자 호출" << std::endl;
    delete [] str;
}

 void string::add_string(const string &s){
     //다시 깔끔하게 짜보기
    typedef struct{
        char* strtemp;
        int lentemp;
    }temp;
    temp tmp;
    tmp.strtemp = this->str;
    tmp.lentemp = this->len;

    this->len += s.len; 
    str = new char [this->len+1];
    for(int i=0;i<this->len;i++){
        if(*(tmp.strtemp)) str[i]= *(tmp.strtemp)++;
        else str[i] = s.str[i-tmp.lentemp];
    }
    str[this->len]=(char)NULL;
    std::cout << str << std::endl;

 }  // str 뒤에 s 를 붙인다.
// void string::copy_string(const string &s);  // str 에 s 를 복사한다.
int string::strlen(){

    //while(*str != \0)

    return this->len;
}    

int main(){

    //string a('i',5); //암시적
    string b ("abcdde");

    string c(b);

    b.add_string(c);

    std::cout<< b.strlen() <<std::endl;

    return 0;
}