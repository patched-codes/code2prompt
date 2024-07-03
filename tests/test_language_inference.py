from code2prompt.utils.language_inference import infer_language

def test_infer_language():
    """ Test the infer_language function."""
    assert infer_language("main.c") == "c"
    assert infer_language("main.cpp") == "cpp"
    assert infer_language("Main.java") == "java"
    assert infer_language("script.js") == "javascript"
    assert infer_language("Program.cs") == "csharp"
    assert infer_language("index.php") == "php"
    assert infer_language("main.go") == "go"
    assert infer_language("lib.rs") == "rust"
    assert infer_language("app.kt") == "kotlin"
    assert infer_language("main.swift") == "swift"
    assert infer_language("Main.scala") == "scala"
    assert infer_language("main.dart") == "dart"
    assert infer_language("script.py") == "python"
    assert infer_language("script.rb") == "ruby"
    assert infer_language("script.pl") == "perl"
    assert infer_language("script.sh") == "bash"
    assert infer_language("script.ps1") == "powershell"
    assert infer_language("index.html") == "html"
    assert infer_language("data.xml") == "xml"
    assert infer_language("query.sql") == "sql"
    assert infer_language("script.m") == "matlab"
    assert infer_language("script.r") == "r"
    assert infer_language("file.txt") == "plaintext"
