import pytest

def get_payload(code,language,args=''):
    return {
        'code':code,
        'args':args,
        'lang':language
    }

def test_get_supported_languages(client):
    response = client.get("api/getLangs")
    assert response.status_code == 200
    assert response.json == ['Python','Java','C','C++']
    
    
def test_get_wrong_uri(client):
    response = client.get("nonexistent/uri")
    assert response.status_code == 404
    

def test_java_compilation(client):
    response = client.post("api/compile",data=
        get_payload(
    """class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}
    ""","Java"
        )
    )
    assert response.status_code == 200
    res = response.json
    assert res['response'] == 'Hello, World!\n'

def test_java_wrong_code_compilation(client):
    response = client.post("api/compile",data=
        get_payload(
    """class no {
    public okay(String[] args) {
        System.out.println("Hello, World!"); 
    }
}
    ""","Java"
        )
    )
    assert response.status_code == 200
    res = response.json
    assert res['response'] == ''
    
def test_java_with_args(client):
    response = client.post("api/compile",data=
        get_payload(
    """import java.util.Scanner;
    class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Enter Name: ");
        Scanner sn = new Scanner(System.in);
        String name = sn.nextLine();
        System.out.println("Hello, " + name + "!");
    }
}
    ""","Java","Tester"
        )
    )
    assert response.status_code == 200
    res = response.json
    assert res['response'] == 'Enter Name: \nHello, Tester!\n'
    