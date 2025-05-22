package promptgenerator.validation;

import java.util.*;

public class ValidationResult {
    private List<String> errors = new ArrayList<>();
    private List<String> hints = new ArrayList<>();

    public void addError(String error) {
        errors.add(error);
    }

    public void merge(ValidationResult other) {
        this.errors.addAll(other.errors);
        this.hints.addAll(other.hints);
    }

    public void setHints(List<String> hints) {
        this.hints = hints;
    }

    public List<String> getErrors() {
        return errors;
    }

    public List<String> getHints() {
        return hints;
    }
    
    public String toText() {
    	String result = "Errors:\n";
    	int i = 1;
    	for (String error : errors) {
    		result += (i + ". " + error + "\n");
    	}
    	i = 1;
    	result += "Hints:\n";
    	for (String hint : hints) {
    		result += (i + ". " + hint + "\n");
    	}
    	return result;
    }

    public boolean hasErrors() {
        return !errors.isEmpty();
    }
    
    public boolean isValid() {
    	return !hasErrors();
    }
    
    public ValidationResult(List<String> errors) {
		super();
		this.errors = errors;
	}
	
	public ValidationResult() {
		super();
		this.errors = new ArrayList<>();
	}
}
