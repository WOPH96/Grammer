템플릿 문장 아래 오는 것이 class Vector 이므로 이 Vector 클래스에 대한 템플릿을 명시하는데, 만약에 밑에 오는 것이 함수일 경우 함수에 대한 템플릿이 됩니다. 

 <> 안에 전달하려는 것을 명시해주면 됩니다. 우리의 Vector 템플릿은 템플릿 인자로 타입을 받게 되는데, 위 경우 T 에 int 가 전달되게 됩니다.

여태까지는 인자로 특정한 '값' 혹은 '객체' 를 전달해왔지만 '타입' 그 자체를 전달한 적은 없었습니다. 하지만 템플릿을 통해 타입을 전달할 수 있게 됩니다.