package promptgenerator.validation.semantic;

import promptgenerator.validation.*;

public interface SemanticValidator<T> {
    ValidationResult validate(T input);
}