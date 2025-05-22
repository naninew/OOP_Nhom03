package promptgenerator.core;

public interface PromptGenerator<T> {
    String generate(T input);
}
