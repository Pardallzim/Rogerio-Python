describe('Triangulo',function(){    
    it('Testando o Triangulo Equilatero', function () {
        expect(classificaTriangulo(5, 5, 5)).toEqual("Equilatero");
        expect(classificaTriangulo(5, 5, 4)).not.toEqual("Equilatero");
    });
    it('Testando o Triangulo Isósceles', function () {
        expect(classificaTriangulo(5, 5, 8)).toEqual("Isósceles");
        expect(classificaTriangulo(5, 5, 5)).not.toEqual("Isósceles");
    });
    it('Testando o Triangulo Escaleno', function () {
        expect(classificaTriangulo(3, 4, 5)).toEqual("Escaleno");
        expect(classificaTriangulo(5, 5, 8)).not.toEqual("Escaleno");
    });
    it('Testando se o valor resulta em um Tiangulo', function () {
        expect(classificaTriangulo(10, 10, 20)).toEqual("Não é um triângulo válido");
        expect(classificaTriangulo(10, 10, 10)).not.toEqual("Não é um triângulo válido");
    });
});