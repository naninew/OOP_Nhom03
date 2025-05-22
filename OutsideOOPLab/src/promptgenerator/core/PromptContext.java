package promptgenerator.core;

import java.util.Set;

public class PromptContext {

    private Object input; // can be WordInfo, ChineseCharacterInfo, etc.
    private PromptSettings settings; // user preferences
    private String inputLanguage;    // e.g., "English", "Chinese", "Japanese"
    private String outputLanguage;   // e.g., "English"
    private Set<PromptPart> includedParts;

    public PromptContext(Object input, PromptSettings settings) {
        this.input = input;
        this.settings = settings;
    }

    public Object getInput() {
        return input;
    }
    
    public void setInput(Object input) {
    	this.input = input;
    }

    public PromptSettings getSettings() {
        return settings;
    }

    public String getInputLanguage() {
        return inputLanguage;
    }

    public String getOutputLanguage() {
        return outputLanguage;
    }

    public boolean isIncludeValidationHints() {
        return settings.isIncludeValidationHints();
    }
    
    public void setInputLanguage(String inputLanguage) {
        this.inputLanguage = inputLanguage;
    }

    public void setOutputLanguage(String outputLanguage) {
        this.outputLanguage = outputLanguage;
    }

    public void setIncludeHints(boolean includeHints) {
        this.settings.setIncludeValidationHints(includeHints);
    }

	public Set<PromptPart> getIncludedParts() {
		return includedParts;
	}

	public void setIncludedParts(Set<PromptPart> includedParts) {
		this.includedParts = includedParts;
	}
    
    
}
