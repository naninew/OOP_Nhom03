package promptgenerator.validation.logical;

import promptgenerator.validation.*;

public interface LogicalValidator<T> {
    ValidationResult validate(T input);
}
