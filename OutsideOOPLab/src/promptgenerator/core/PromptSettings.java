package promptgenerator.core;

import java.util.*;

public class PromptSettings {
    private boolean simplifyExamples;
    private boolean conciseMode;  // e.g., for flashcard back side
    private int characterLimit = 300;   // max characters in output
    private boolean includeValidationHints;
    private boolean allowPartialInput;
	public boolean isSimplifyExamples() {
		return simplifyExamples;
	}
	
	public void setSimplifyExamples(boolean simplifyExamples) {
		this.simplifyExamples = simplifyExamples;
	}
	
	public boolean isConciseMode() {
		return conciseMode;
	}
	
	public void setConciseMode(boolean conciseMode) {
		this.conciseMode = conciseMode;
	}
	
	public int getCharacterLimit() {
		return characterLimit;
	}
	
	public void setCharacterLimit(int characterLimit) {
		this.characterLimit = characterLimit;
	}
	
	public boolean isIncludeValidationHints() {
		return includeValidationHints;
	}
	
	public void setIncludeValidationHints(boolean includeValidationHints) {
		this.includeValidationHints = includeValidationHints;
	}
	
	public boolean isAllowPartialInput() {
		return allowPartialInput;
	}
	
	public void setAllowPartialInput(boolean allowPartialInput) {
		this.allowPartialInput = allowPartialInput;
	}
}