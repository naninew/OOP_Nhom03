package promptgenerator.core;

import java.util.*;

public class PromptSettings {
    private boolean conciseMode;  // e.g., for flashcard back side
    private int characterLimit = 300;   // max characters in output
    private boolean includeValidationHints = false;
	
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
}