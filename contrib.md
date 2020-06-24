# Contributions



## Samples

Samples are organized into subpacks and largely consists of instrument samples,
such as for pitched instruments, synthesizers, or percussion. We are not
currently accepting things like canned loops or speech samples, although 
samples consisting of singing or humming. In some circumstances, recordings of
chords may also be warranted (for instance, on a polyphonic instrument such as
a piano or guitar).

The sample should be recording as a 16-bit signed, 44.1KHz WAV and should be as
short as reasonably possible without sacrificing quality. When recording a 
sample, remove any silence preceeding the attack phase (the "beginning") of the
sample and truncate any silence following the end of its release (when the 
instrument is no longer sounded). In many cases this may be a judgement call:
it is generally preferrable to allow an accoustic instrument to "ring" if 
possible. However, for an instrument with unbounded sustain, only the portions
needed to replicate the sustain should be recorded.

###Candidacy

Many instruments have multiple modes of operation. For instance, a guitar can be
picked or strummed, a bass guitar may be plucked or slapped, and a violin may
either be bowed or plucked (i.e., pizzacato). It is reasonable to have separate
recordings representing each of these playing styles to preserve their timbre.
Some instruments have a continuous range of timbre by virtue of being 
parameterized; this includes many synthesizers, but may also include 
instruments like the Wurlitzer 200A (which has a vibrato pot on it). What to do
in this circumstance is a judgement call that may be influenced by the 
following factors:

- Is it difficult to model the sample through programmatic or other means (e.g., 
 ADSR envelope) to produce the sample in question?
- Is there a reasonable "clean" state which represents the instrument in 
 question in some sort of "natural" or "basal" state which can be used to
 derive many other samples?
- Is the sample such a common use case such that its exclusion would be a 
 glaring omission?
 
 If any of these criteria are met, it is likely a good candidate for being 
 included as a sample. To give an idea of what might qualify, some examples are
 provided:
 
 - A piano sample (due to its inharmonic frequencies) may be difficult to model
  properly and should probably be included.
 - A guitar sample is less so, but still may nonetheless be difficult to model
  accuractely, particularly if the timbre of a specific model is sought.
 - The Wurlitzer 200A's signal with no vibrato has few overtones and may be
  simple to model, but can be used to derive many other waveforms via the 
  envelope.
 - Primitive waveforms such as sine or square waves are clean forms of their
  their signal and are such a common use case that their omission would be a
  glaring omission.
 - Aliased square waves are easy to model with a Taylor series, but are such
  a common waveform that their omission would be a glaring omission.
 - The Wurlitzer 200A at full vibrato is such a common use case for that
  instrument that its exclusion would be a glaring oversight.
  
 Conversely, it is reasonable to talk about what makes bad candidates for 
 inclusion into the sample library. The following are examples of candidates
 that should not be inlcuded in WOSL:
 
 - A square wave at 37% duty cycle. This can be easily generated on the fly,
 is an adulterated form of a 50% duty cycle square wave, and would have a niche
 application.
 - The DX7 (generally) as an instrument. Individual patches may be candidates 
 for sampling (although the copyright question is a big one here), but there is
 no "clean" state for a DX7.
 - The Wurlitzer 200A at 50% vibrato. The signal is not clean and full vibrato
 is usually the most common alternative.
 
Note that this does not mean that other mechanisms can't be included to provide
this functionality. For instance, the above square wave or DX7 emulation could
be provided by a script, while the the Wurlitzer could be done through the ADSR
envelope.

The samples need not be intriniscally musical themselves and may be included as
long as they meet the above requirements. For instance, a sample of flatulance
or a car engine cranking is appropriate for this pack.

### File Structure

Samples are placed into  sample collections, which are directories containing 
related samples. Each sample collection belongs to a category, which itself 
belongs to the "sample" directory in the repository root. For instance, the 
following facts can be known just by looking at the path 
"*samples/guitars/reson8r*":

- It contains samples related to collection named *reson8r*
- It is in the *guitar* category

Sample collections may have subdirectories indicating subclasses related to
the sample collection. For instance, the *reson8r* sample colleciton contains
a *chords* subdirectory which is designated for chord sample. Samples
collections are not required to have such sample subclasses.

By itself, you would know little else about this sample collection. For 
instance, you may not be familiar with what a reson8r is, what model reson8r
is being recorded, and how it was recorded. A series of README.md files 
should be included to eludicate on the details. For instance, one may
learn more information about the "reson8r" sample collection by viewing its
[readme.md](samples/guitars/reson8r/readme.md). In the future, other metadata
may be included.

Sample names are in 8.3 format to preserve usability with legacy environments.
It is conceivable that they will be used in environments such as MS-DOS or
vintage samplers. Conversely, modern operating systems have no problem with
this restriction.

When contributing a sample, select the most appropriate category and create
a descriptive name under that directory. If an appropriate category does not
exist, create it and its corresponding README.md (see below). Next, select 
the corresponding sample collection. If one does not exist (which is likely),
you may create one with the corresponding README.md. Otherwise, consult the
README.md and amend as necessary. Generally speaking, you should create a new
collection if it does not fit the description of any sample collection 
according to its README.md. 

When determining what to name samples, consult the associated readme. Note
that readmes are heirarchical, so you may need to also consult the readme
corresponding to the category according to the Nested Documentation Rule
described below. Generally speaking, the format is the following:

- *x*-*method*.wav for pitched instruments, where *x* is the tonic or root
note of sample being recorded.
- *name*.wav for others, where *name* is a descriptive name for the sample.

When possible, prefer the naming conventions already specified by the sample
collection or category. If no convention is sufficient, invent your own with
a reasonable name, but try to accomodate the existing categories if possible.

### Metadata

Metadata is provided for each category and sample collection to make it easier
to work with. The item should contain a markdown file called readme.md. 
Typically, this metadata is provides a brief synopsis of the item in question,
along with any pertinent details corresponding to it. Common details include 
playing methods associated with the sample collection, any pitch respelling, 
and a description of how the sample was recorded and if it applies to a 
specific source (like a particular model of instrument). Any conventions used
by the sample collection should be listed in this file.

Documentation is inherited, meaning that any documentation that applies to the
item's parent also applies to it. For instance, documentation that applies to
the "samples/guitars" category also applies to "samples/guitars/reson8tr". This
is allowed to be overridden by the descendent's documentation: the 
documentation for reson8tr may override or redact documentation specified by
the guitar category. In fact, there is a [readme.md](samples/readme.md) for
the entire sample repository (todo: not implemented).