package promptgenerator.validation.wip_semantic;

import promptgenerator.validation.*;

public interface SemanticValidator<T> {
    ValidationResult validate(T input);
}