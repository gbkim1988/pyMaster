# pyDesignPattern

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

## Python Factory Pattern

Factory 패턴의 부재는 "Encapsulating Object Creation(객체 생성 캡슐화)"
변경 요구 사항 중 다음의 사례인 경우 Factory Pattern 을 사용하기에 용이하다.
- 새로운 타입(클래스)를 위한 공통 인터페이스를 생성하기 위해서 다형성(polymorphism) 개념을 사용할 수 있다.
  추가하려는 뉴 타입의 지식으로부터 기존 코드를 분리시킬 수 있다.

      곁생각_START>
          파이썬은 타입 체크를 하지 않는 언어이다. 이로 인해 해당 객체의 상위 클래스로 타입을 지정하여 하위 객체들을
          포함하는 구현방법은 의미가 없다.

            파이썬에게는 단순히 논리적인 객체를 사용하는 포로토콜에 불과하다. 그렇다면 이러한 객체의 상속구조를
            유지시킬 필요가 있을까?

            나의 대답은 그렇다이다. 우선, 상속을 통해서 약속을 문서화하는 과정이 매우 중요하다. (물론 구조를 잘 짜는 것도 중요
            하겠지만...)
      곁생각_END>
- 결론부터 말하자면, 객체를 생성하는 객체를 생성하는 것이다. 모든 코드가 객체 생성 객체(Factory)를 통하여 생성된다면,
  이를 사용하는 모든 코드들은 어떠한 객체가 생성된다는 약속하여, 이를 포괄하는 코드를 작성하게될 것이다.

  예를들어, 동물팩토리를 사용할 경우, 동물팩토리가 개, 고양이, 등등 다양한 개체를 생성한다는 사실을 알고 있고,
  이 개체들을 사용하는 방법에는 "bark", "feed" 가 있다는 것을 알 수 있다.
  이러한 약속과 지식을 토대로 나머지 코드를 갖추어 나간다.



      곁생각_START>
          고양이, 개는 동물이다.
          개는 '멍멍' 이라고 말한다.
          아직, 고양이의 울움소리는 밝혀지지 않았다. 하지만, 존재하는 동물이다.
          개의 소리를 녹음하여 개의 심리상태를 알려주는 시스템이 존재한다.
          여러 종류의 개의 목소리를 녹음하고, 이를 분석한 데이터가 존재한다.
          이러한 데이터는 다양한 계층으로 분할되어 중간데이터 역할을 한다.

          이때에, 가장 편리하게, 고양이의 데이터를 모든 시스템에 적용할 방법은 무엇인가?
      곁생각_END>

## 다형성(polymorphism) 이란?
Trace : Python Factory Pattern > Polymorphism

In programming languages and type theory, polymorphism (from Greek πολύς, polys, "many, much" and μορφή, morphē,
"form, shape") is the provision of a single interface to entities of different types.
> 다양한 타입의 객체에 대한 단일 인터페이를 제공하는 것이 polymorphism

