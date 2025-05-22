package promptgenerator.model;

import java.util.*;

public class WordInfo {
    private String word;
    private String language;
    private String wordLevel;
    private List<String> wordTypes; // noun, verb, etc.
    
    public boolean isEmpty() {
    	if (word == null || word.trim().isEmpty()) {
    		return true;
    	}
    	return false;
    }

	public WordInfo(String word, String language, String wordLevel, List<String> wordTypes) {
		super();
		this.word = word;
		this.language = language;
		this.wordLevel = wordLevel;
		this.wordTypes = wordTypes;
	}

	public String getLanguage() {
		return language;
	}

	public void setLanguage(String language) {
		this.language = language;
	}

	public String getWordLevel() {
		return wordLevel;
	}

	public void setWordLevel(String wordLevel) {
		this.wordLevel = wordLevel;
	}

	public List<String> getWordTypes() {
		return wordTypes;
	}

	public void setWordTypes(List<String> wordTypes) {
		this.wordTypes = wordTypes;
	}
	
	public String getWord() {
		return word;
	}

	public void setWord(String word) {
		this.word = word;
	}
}
