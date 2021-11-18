// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: service.proto

/**
 * Protobuf type {@code AlterarNotaRequest}
 */
public  final class AlterarNotaRequest extends
    com.google.protobuf.GeneratedMessageV3 implements
    // @@protoc_insertion_point(message_implements:AlterarNotaRequest)
    AlterarNotaRequestOrBuilder {
  // Use AlterarNotaRequest.newBuilder() to construct.
  private AlterarNotaRequest(com.google.protobuf.GeneratedMessageV3.Builder<?> builder) {
    super(builder);
  }
  private AlterarNotaRequest() {
    ra_ = 0;
    codigoDisciplina_ = "";
    ano_ = 0;
    semestre_ = 0;
    nota_ = 0F;
  }

  @java.lang.Override
  public final com.google.protobuf.UnknownFieldSet
  getUnknownFields() {
    return com.google.protobuf.UnknownFieldSet.getDefaultInstance();
  }
  private AlterarNotaRequest(
      com.google.protobuf.CodedInputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    this();
    int mutable_bitField0_ = 0;
    try {
      boolean done = false;
      while (!done) {
        int tag = input.readTag();
        switch (tag) {
          case 0:
            done = true;
            break;
          default: {
            if (!input.skipField(tag)) {
              done = true;
            }
            break;
          }
          case 8: {

            ra_ = input.readInt32();
            break;
          }
          case 18: {
            java.lang.String s = input.readStringRequireUtf8();

            codigoDisciplina_ = s;
            break;
          }
          case 24: {

            ano_ = input.readInt32();
            break;
          }
          case 32: {

            semestre_ = input.readInt32();
            break;
          }
          case 45: {

            nota_ = input.readFloat();
            break;
          }
        }
      }
    } catch (com.google.protobuf.InvalidProtocolBufferException e) {
      throw e.setUnfinishedMessage(this);
    } catch (java.io.IOException e) {
      throw new com.google.protobuf.InvalidProtocolBufferException(
          e).setUnfinishedMessage(this);
    } finally {
      makeExtensionsImmutable();
    }
  }
  public static final com.google.protobuf.Descriptors.Descriptor
      getDescriptor() {
    return HelloWorldProto.internal_static_AlterarNotaRequest_descriptor;
  }

  protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internalGetFieldAccessorTable() {
    return HelloWorldProto.internal_static_AlterarNotaRequest_fieldAccessorTable
        .ensureFieldAccessorsInitialized(
            AlterarNotaRequest.class, AlterarNotaRequest.Builder.class);
  }

  public static final int RA_FIELD_NUMBER = 1;
  private int ra_;
  /**
   * <code>int32 ra = 1;</code>
   */
  public int getRa() {
    return ra_;
  }

  public static final int CODIGODISCIPLINA_FIELD_NUMBER = 2;
  private volatile java.lang.Object codigoDisciplina_;
  /**
   * <code>string codigoDisciplina = 2;</code>
   */
  public java.lang.String getCodigoDisciplina() {
    java.lang.Object ref = codigoDisciplina_;
    if (ref instanceof java.lang.String) {
      return (java.lang.String) ref;
    } else {
      com.google.protobuf.ByteString bs = 
          (com.google.protobuf.ByteString) ref;
      java.lang.String s = bs.toStringUtf8();
      codigoDisciplina_ = s;
      return s;
    }
  }
  /**
   * <code>string codigoDisciplina = 2;</code>
   */
  public com.google.protobuf.ByteString
      getCodigoDisciplinaBytes() {
    java.lang.Object ref = codigoDisciplina_;
    if (ref instanceof java.lang.String) {
      com.google.protobuf.ByteString b = 
          com.google.protobuf.ByteString.copyFromUtf8(
              (java.lang.String) ref);
      codigoDisciplina_ = b;
      return b;
    } else {
      return (com.google.protobuf.ByteString) ref;
    }
  }

  public static final int ANO_FIELD_NUMBER = 3;
  private int ano_;
  /**
   * <code>int32 ano = 3;</code>
   */
  public int getAno() {
    return ano_;
  }

  public static final int SEMESTRE_FIELD_NUMBER = 4;
  private int semestre_;
  /**
   * <code>int32 semestre = 4;</code>
   */
  public int getSemestre() {
    return semestre_;
  }

  public static final int NOTA_FIELD_NUMBER = 5;
  private float nota_;
  /**
   * <code>float nota = 5;</code>
   */
  public float getNota() {
    return nota_;
  }

  private byte memoizedIsInitialized = -1;
  public final boolean isInitialized() {
    byte isInitialized = memoizedIsInitialized;
    if (isInitialized == 1) return true;
    if (isInitialized == 0) return false;

    memoizedIsInitialized = 1;
    return true;
  }

  public void writeTo(com.google.protobuf.CodedOutputStream output)
                      throws java.io.IOException {
    if (ra_ != 0) {
      output.writeInt32(1, ra_);
    }
    if (!getCodigoDisciplinaBytes().isEmpty()) {
      com.google.protobuf.GeneratedMessageV3.writeString(output, 2, codigoDisciplina_);
    }
    if (ano_ != 0) {
      output.writeInt32(3, ano_);
    }
    if (semestre_ != 0) {
      output.writeInt32(4, semestre_);
    }
    if (nota_ != 0F) {
      output.writeFloat(5, nota_);
    }
  }

  public int getSerializedSize() {
    int size = memoizedSize;
    if (size != -1) return size;

    size = 0;
    if (ra_ != 0) {
      size += com.google.protobuf.CodedOutputStream
        .computeInt32Size(1, ra_);
    }
    if (!getCodigoDisciplinaBytes().isEmpty()) {
      size += com.google.protobuf.GeneratedMessageV3.computeStringSize(2, codigoDisciplina_);
    }
    if (ano_ != 0) {
      size += com.google.protobuf.CodedOutputStream
        .computeInt32Size(3, ano_);
    }
    if (semestre_ != 0) {
      size += com.google.protobuf.CodedOutputStream
        .computeInt32Size(4, semestre_);
    }
    if (nota_ != 0F) {
      size += com.google.protobuf.CodedOutputStream
        .computeFloatSize(5, nota_);
    }
    memoizedSize = size;
    return size;
  }

  private static final long serialVersionUID = 0L;
  @java.lang.Override
  public boolean equals(final java.lang.Object obj) {
    if (obj == this) {
     return true;
    }
    if (!(obj instanceof AlterarNotaRequest)) {
      return super.equals(obj);
    }
    AlterarNotaRequest other = (AlterarNotaRequest) obj;

    boolean result = true;
    result = result && (getRa()
        == other.getRa());
    result = result && getCodigoDisciplina()
        .equals(other.getCodigoDisciplina());
    result = result && (getAno()
        == other.getAno());
    result = result && (getSemestre()
        == other.getSemestre());
    result = result && (
        java.lang.Float.floatToIntBits(getNota())
        == java.lang.Float.floatToIntBits(
            other.getNota()));
    return result;
  }

  @java.lang.Override
  public int hashCode() {
    if (memoizedHashCode != 0) {
      return memoizedHashCode;
    }
    int hash = 41;
    hash = (19 * hash) + getDescriptor().hashCode();
    hash = (37 * hash) + RA_FIELD_NUMBER;
    hash = (53 * hash) + getRa();
    hash = (37 * hash) + CODIGODISCIPLINA_FIELD_NUMBER;
    hash = (53 * hash) + getCodigoDisciplina().hashCode();
    hash = (37 * hash) + ANO_FIELD_NUMBER;
    hash = (53 * hash) + getAno();
    hash = (37 * hash) + SEMESTRE_FIELD_NUMBER;
    hash = (53 * hash) + getSemestre();
    hash = (37 * hash) + NOTA_FIELD_NUMBER;
    hash = (53 * hash) + java.lang.Float.floatToIntBits(
        getNota());
    hash = (29 * hash) + unknownFields.hashCode();
    memoizedHashCode = hash;
    return hash;
  }

  public static AlterarNotaRequest parseFrom(
      java.nio.ByteBuffer data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static AlterarNotaRequest parseFrom(
      java.nio.ByteBuffer data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static AlterarNotaRequest parseFrom(
      com.google.protobuf.ByteString data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static AlterarNotaRequest parseFrom(
      com.google.protobuf.ByteString data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static AlterarNotaRequest parseFrom(byte[] data)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data);
  }
  public static AlterarNotaRequest parseFrom(
      byte[] data,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws com.google.protobuf.InvalidProtocolBufferException {
    return PARSER.parseFrom(data, extensionRegistry);
  }
  public static AlterarNotaRequest parseFrom(java.io.InputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input);
  }
  public static AlterarNotaRequest parseFrom(
      java.io.InputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input, extensionRegistry);
  }
  public static AlterarNotaRequest parseDelimitedFrom(java.io.InputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseDelimitedWithIOException(PARSER, input);
  }
  public static AlterarNotaRequest parseDelimitedFrom(
      java.io.InputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseDelimitedWithIOException(PARSER, input, extensionRegistry);
  }
  public static AlterarNotaRequest parseFrom(
      com.google.protobuf.CodedInputStream input)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input);
  }
  public static AlterarNotaRequest parseFrom(
      com.google.protobuf.CodedInputStream input,
      com.google.protobuf.ExtensionRegistryLite extensionRegistry)
      throws java.io.IOException {
    return com.google.protobuf.GeneratedMessageV3
        .parseWithIOException(PARSER, input, extensionRegistry);
  }

  public Builder newBuilderForType() { return newBuilder(); }
  public static Builder newBuilder() {
    return DEFAULT_INSTANCE.toBuilder();
  }
  public static Builder newBuilder(AlterarNotaRequest prototype) {
    return DEFAULT_INSTANCE.toBuilder().mergeFrom(prototype);
  }
  public Builder toBuilder() {
    return this == DEFAULT_INSTANCE
        ? new Builder() : new Builder().mergeFrom(this);
  }

  @java.lang.Override
  protected Builder newBuilderForType(
      com.google.protobuf.GeneratedMessageV3.BuilderParent parent) {
    Builder builder = new Builder(parent);
    return builder;
  }
  /**
   * Protobuf type {@code AlterarNotaRequest}
   */
  public static final class Builder extends
      com.google.protobuf.GeneratedMessageV3.Builder<Builder> implements
      // @@protoc_insertion_point(builder_implements:AlterarNotaRequest)
      AlterarNotaRequestOrBuilder {
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return HelloWorldProto.internal_static_AlterarNotaRequest_descriptor;
    }

    protected com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return HelloWorldProto.internal_static_AlterarNotaRequest_fieldAccessorTable
          .ensureFieldAccessorsInitialized(
              AlterarNotaRequest.class, AlterarNotaRequest.Builder.class);
    }

    // Construct using AlterarNotaRequest.newBuilder()
    private Builder() {
      maybeForceBuilderInitialization();
    }

    private Builder(
        com.google.protobuf.GeneratedMessageV3.BuilderParent parent) {
      super(parent);
      maybeForceBuilderInitialization();
    }
    private void maybeForceBuilderInitialization() {
      if (com.google.protobuf.GeneratedMessageV3
              .alwaysUseFieldBuilders) {
      }
    }
    public Builder clear() {
      super.clear();
      ra_ = 0;

      codigoDisciplina_ = "";

      ano_ = 0;

      semestre_ = 0;

      nota_ = 0F;

      return this;
    }

    public com.google.protobuf.Descriptors.Descriptor
        getDescriptorForType() {
      return HelloWorldProto.internal_static_AlterarNotaRequest_descriptor;
    }

    public AlterarNotaRequest getDefaultInstanceForType() {
      return AlterarNotaRequest.getDefaultInstance();
    }

    public AlterarNotaRequest build() {
      AlterarNotaRequest result = buildPartial();
      if (!result.isInitialized()) {
        throw newUninitializedMessageException(result);
      }
      return result;
    }

    public AlterarNotaRequest buildPartial() {
      AlterarNotaRequest result = new AlterarNotaRequest(this);
      result.ra_ = ra_;
      result.codigoDisciplina_ = codigoDisciplina_;
      result.ano_ = ano_;
      result.semestre_ = semestre_;
      result.nota_ = nota_;
      onBuilt();
      return result;
    }

    public Builder clone() {
      return (Builder) super.clone();
    }
    public Builder setField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        Object value) {
      return (Builder) super.setField(field, value);
    }
    public Builder clearField(
        com.google.protobuf.Descriptors.FieldDescriptor field) {
      return (Builder) super.clearField(field);
    }
    public Builder clearOneof(
        com.google.protobuf.Descriptors.OneofDescriptor oneof) {
      return (Builder) super.clearOneof(oneof);
    }
    public Builder setRepeatedField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        int index, Object value) {
      return (Builder) super.setRepeatedField(field, index, value);
    }
    public Builder addRepeatedField(
        com.google.protobuf.Descriptors.FieldDescriptor field,
        Object value) {
      return (Builder) super.addRepeatedField(field, value);
    }
    public Builder mergeFrom(com.google.protobuf.Message other) {
      if (other instanceof AlterarNotaRequest) {
        return mergeFrom((AlterarNotaRequest)other);
      } else {
        super.mergeFrom(other);
        return this;
      }
    }

    public Builder mergeFrom(AlterarNotaRequest other) {
      if (other == AlterarNotaRequest.getDefaultInstance()) return this;
      if (other.getRa() != 0) {
        setRa(other.getRa());
      }
      if (!other.getCodigoDisciplina().isEmpty()) {
        codigoDisciplina_ = other.codigoDisciplina_;
        onChanged();
      }
      if (other.getAno() != 0) {
        setAno(other.getAno());
      }
      if (other.getSemestre() != 0) {
        setSemestre(other.getSemestre());
      }
      if (other.getNota() != 0F) {
        setNota(other.getNota());
      }
      onChanged();
      return this;
    }

    public final boolean isInitialized() {
      return true;
    }

    public Builder mergeFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      AlterarNotaRequest parsedMessage = null;
      try {
        parsedMessage = PARSER.parsePartialFrom(input, extensionRegistry);
      } catch (com.google.protobuf.InvalidProtocolBufferException e) {
        parsedMessage = (AlterarNotaRequest) e.getUnfinishedMessage();
        throw e.unwrapIOException();
      } finally {
        if (parsedMessage != null) {
          mergeFrom(parsedMessage);
        }
      }
      return this;
    }

    private int ra_ ;
    /**
     * <code>int32 ra = 1;</code>
     */
    public int getRa() {
      return ra_;
    }
    /**
     * <code>int32 ra = 1;</code>
     */
    public Builder setRa(int value) {
      
      ra_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>int32 ra = 1;</code>
     */
    public Builder clearRa() {
      
      ra_ = 0;
      onChanged();
      return this;
    }

    private java.lang.Object codigoDisciplina_ = "";
    /**
     * <code>string codigoDisciplina = 2;</code>
     */
    public java.lang.String getCodigoDisciplina() {
      java.lang.Object ref = codigoDisciplina_;
      if (!(ref instanceof java.lang.String)) {
        com.google.protobuf.ByteString bs =
            (com.google.protobuf.ByteString) ref;
        java.lang.String s = bs.toStringUtf8();
        codigoDisciplina_ = s;
        return s;
      } else {
        return (java.lang.String) ref;
      }
    }
    /**
     * <code>string codigoDisciplina = 2;</code>
     */
    public com.google.protobuf.ByteString
        getCodigoDisciplinaBytes() {
      java.lang.Object ref = codigoDisciplina_;
      if (ref instanceof String) {
        com.google.protobuf.ByteString b = 
            com.google.protobuf.ByteString.copyFromUtf8(
                (java.lang.String) ref);
        codigoDisciplina_ = b;
        return b;
      } else {
        return (com.google.protobuf.ByteString) ref;
      }
    }
    /**
     * <code>string codigoDisciplina = 2;</code>
     */
    public Builder setCodigoDisciplina(
        java.lang.String value) {
      if (value == null) {
    throw new NullPointerException();
  }
  
      codigoDisciplina_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>string codigoDisciplina = 2;</code>
     */
    public Builder clearCodigoDisciplina() {
      
      codigoDisciplina_ = getDefaultInstance().getCodigoDisciplina();
      onChanged();
      return this;
    }
    /**
     * <code>string codigoDisciplina = 2;</code>
     */
    public Builder setCodigoDisciplinaBytes(
        com.google.protobuf.ByteString value) {
      if (value == null) {
    throw new NullPointerException();
  }
  checkByteStringIsUtf8(value);
      
      codigoDisciplina_ = value;
      onChanged();
      return this;
    }

    private int ano_ ;
    /**
     * <code>int32 ano = 3;</code>
     */
    public int getAno() {
      return ano_;
    }
    /**
     * <code>int32 ano = 3;</code>
     */
    public Builder setAno(int value) {
      
      ano_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>int32 ano = 3;</code>
     */
    public Builder clearAno() {
      
      ano_ = 0;
      onChanged();
      return this;
    }

    private int semestre_ ;
    /**
     * <code>int32 semestre = 4;</code>
     */
    public int getSemestre() {
      return semestre_;
    }
    /**
     * <code>int32 semestre = 4;</code>
     */
    public Builder setSemestre(int value) {
      
      semestre_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>int32 semestre = 4;</code>
     */
    public Builder clearSemestre() {
      
      semestre_ = 0;
      onChanged();
      return this;
    }

    private float nota_ ;
    /**
     * <code>float nota = 5;</code>
     */
    public float getNota() {
      return nota_;
    }
    /**
     * <code>float nota = 5;</code>
     */
    public Builder setNota(float value) {
      
      nota_ = value;
      onChanged();
      return this;
    }
    /**
     * <code>float nota = 5;</code>
     */
    public Builder clearNota() {
      
      nota_ = 0F;
      onChanged();
      return this;
    }
    public final Builder setUnknownFields(
        final com.google.protobuf.UnknownFieldSet unknownFields) {
      return this;
    }

    public final Builder mergeUnknownFields(
        final com.google.protobuf.UnknownFieldSet unknownFields) {
      return this;
    }


    // @@protoc_insertion_point(builder_scope:AlterarNotaRequest)
  }

  // @@protoc_insertion_point(class_scope:AlterarNotaRequest)
  private static final AlterarNotaRequest DEFAULT_INSTANCE;
  static {
    DEFAULT_INSTANCE = new AlterarNotaRequest();
  }

  public static AlterarNotaRequest getDefaultInstance() {
    return DEFAULT_INSTANCE;
  }

  private static final com.google.protobuf.Parser<AlterarNotaRequest>
      PARSER = new com.google.protobuf.AbstractParser<AlterarNotaRequest>() {
    public AlterarNotaRequest parsePartialFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
        return new AlterarNotaRequest(input, extensionRegistry);
    }
  };

  public static com.google.protobuf.Parser<AlterarNotaRequest> parser() {
    return PARSER;
  }

  @java.lang.Override
  public com.google.protobuf.Parser<AlterarNotaRequest> getParserForType() {
    return PARSER;
  }

  public AlterarNotaRequest getDefaultInstanceForType() {
    return DEFAULT_INSTANCE;
  }

}

