package promptgenerator.validation.logical;

import promptgenerator.validation.*;
import promptgenerator.model.*;

public class RadicalInfoValidator implements LogicalValidator<RadicalInfo> {
    public ValidationResult validate(RadicalInfo radicalInfo) {
        ValidationResult result = new ValidationResult();
        if (radicalInfo.getRadical() == null || radicalInfo.getRadical().isEmpty()) {
            result.addError("Radical cannot be empty.");
        }
        return result;
    }
}
