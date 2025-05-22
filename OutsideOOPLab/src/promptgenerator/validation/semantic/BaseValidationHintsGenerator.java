package promptgenerator.validation.semantic;

import java.util.*;

import promptgenerator.core.*;
import promptgenerator.validation.*;

public abstract class BaseValidationHintsGenerator<T> implements SemanticValidator<T> {

    protected PromptContext context;

    public BaseValidationHintsGenerator(PromptContext context) {
        this.context = context;
    }

    protected abstract List<String> checkInferableFields(T input);

    @Override
    public ValidationResult validate(T input) {
        List<String> hints = checkInferableFields(input);
        ValidationResult validationResult = new ValidationResult(hints); // just one list, not separating errors/hints yet
        return validationResult;
    }
}
