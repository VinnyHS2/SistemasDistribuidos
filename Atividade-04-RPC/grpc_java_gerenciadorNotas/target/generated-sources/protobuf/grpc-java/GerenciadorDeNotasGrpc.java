import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.asyncServerStreamingCall;
import static io.grpc.stub.ClientCalls.asyncClientStreamingCall;
import static io.grpc.stub.ClientCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.blockingServerStreamingCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncServerStreamingCall;
import static io.grpc.stub.ServerCalls.asyncClientStreamingCall;
import static io.grpc.stub.ServerCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedStreamingCall;

/**
 * <pre>
 * interface de serviço
 * </pre>
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.4.0)",
    comments = "Source: service.proto")
public final class GerenciadorDeNotasGrpc {

  private GerenciadorDeNotasGrpc() {}

  public static final String SERVICE_NAME = "GerenciadorDeNotas";

  // Static method descriptors that strictly reflect the proto.
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<ListarAlunosRequest,
      ListarAlunosResponse> METHOD_LISTAR_ALUNOS =
      io.grpc.MethodDescriptor.<ListarAlunosRequest, ListarAlunosResponse>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "GerenciadorDeNotas", "ListarAlunos"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              ListarAlunosRequest.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              ListarAlunosResponse.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<AlterarNotaRequest,
      AlterarNotaResponse> METHOD_ALTERAR_NOTA =
      io.grpc.MethodDescriptor.<AlterarNotaRequest, AlterarNotaResponse>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "GerenciadorDeNotas", "AlterarNota"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              AlterarNotaRequest.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              AlterarNotaResponse.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<AlterarFaltasRequest,
      AlterarFaltasResponse> METHOD_ALTERAR_FALTAS =
      io.grpc.MethodDescriptor.<AlterarFaltasRequest, AlterarFaltasResponse>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "GerenciadorDeNotas", "AlterarFaltas"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              AlterarFaltasRequest.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              AlterarFaltasResponse.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<ListarDisciplinasCursoRequest,
      ListarDisciplinasCursoResponse> METHOD_LISTAR_DISCIPLINAS_CURSO =
      io.grpc.MethodDescriptor.<ListarDisciplinasCursoRequest, ListarDisciplinasCursoResponse>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "GerenciadorDeNotas", "ListarDisciplinasCurso"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              ListarDisciplinasCursoRequest.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              ListarDisciplinasCursoResponse.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<ListarDisciplinasAlunoRequest,
      ListarDisciplinasAlunoResponse> METHOD_LISTAR_DISCIPLINAS_ALUNO =
      io.grpc.MethodDescriptor.<ListarDisciplinasAlunoRequest, ListarDisciplinasAlunoResponse>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "GerenciadorDeNotas", "ListarDisciplinasAluno"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              ListarDisciplinasAlunoRequest.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              ListarDisciplinasAlunoResponse.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<InserirMatriculaRequest,
      InserirMatriculaResponse> METHOD_INSERIR_MATRICULA =
      io.grpc.MethodDescriptor.<InserirMatriculaRequest, InserirMatriculaResponse>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "GerenciadorDeNotas", "InserirMatricula"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              InserirMatriculaRequest.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              InserirMatriculaResponse.getDefaultInstance()))
          .build();

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static GerenciadorDeNotasStub newStub(io.grpc.Channel channel) {
    return new GerenciadorDeNotasStub(channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static GerenciadorDeNotasBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    return new GerenciadorDeNotasBlockingStub(channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static GerenciadorDeNotasFutureStub newFutureStub(
      io.grpc.Channel channel) {
    return new GerenciadorDeNotasFutureStub(channel);
  }

  /**
   * <pre>
   * interface de serviço
   * </pre>
   */
  public static abstract class GerenciadorDeNotasImplBase implements io.grpc.BindableService {

    /**
     */
    public void listarAlunos(ListarAlunosRequest request,
        io.grpc.stub.StreamObserver<ListarAlunosResponse> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_LISTAR_ALUNOS, responseObserver);
    }

    /**
     */
    public void alterarNota(AlterarNotaRequest request,
        io.grpc.stub.StreamObserver<AlterarNotaResponse> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_ALTERAR_NOTA, responseObserver);
    }

    /**
     */
    public void alterarFaltas(AlterarFaltasRequest request,
        io.grpc.stub.StreamObserver<AlterarFaltasResponse> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_ALTERAR_FALTAS, responseObserver);
    }

    /**
     */
    public void listarDisciplinasCurso(ListarDisciplinasCursoRequest request,
        io.grpc.stub.StreamObserver<ListarDisciplinasCursoResponse> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_LISTAR_DISCIPLINAS_CURSO, responseObserver);
    }

    /**
     */
    public void listarDisciplinasAluno(ListarDisciplinasAlunoRequest request,
        io.grpc.stub.StreamObserver<ListarDisciplinasAlunoResponse> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_LISTAR_DISCIPLINAS_ALUNO, responseObserver);
    }

    /**
     */
    public void inserirMatricula(InserirMatriculaRequest request,
        io.grpc.stub.StreamObserver<InserirMatriculaResponse> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_INSERIR_MATRICULA, responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            METHOD_LISTAR_ALUNOS,
            asyncUnaryCall(
              new MethodHandlers<
                ListarAlunosRequest,
                ListarAlunosResponse>(
                  this, METHODID_LISTAR_ALUNOS)))
          .addMethod(
            METHOD_ALTERAR_NOTA,
            asyncUnaryCall(
              new MethodHandlers<
                AlterarNotaRequest,
                AlterarNotaResponse>(
                  this, METHODID_ALTERAR_NOTA)))
          .addMethod(
            METHOD_ALTERAR_FALTAS,
            asyncUnaryCall(
              new MethodHandlers<
                AlterarFaltasRequest,
                AlterarFaltasResponse>(
                  this, METHODID_ALTERAR_FALTAS)))
          .addMethod(
            METHOD_LISTAR_DISCIPLINAS_CURSO,
            asyncUnaryCall(
              new MethodHandlers<
                ListarDisciplinasCursoRequest,
                ListarDisciplinasCursoResponse>(
                  this, METHODID_LISTAR_DISCIPLINAS_CURSO)))
          .addMethod(
            METHOD_LISTAR_DISCIPLINAS_ALUNO,
            asyncUnaryCall(
              new MethodHandlers<
                ListarDisciplinasAlunoRequest,
                ListarDisciplinasAlunoResponse>(
                  this, METHODID_LISTAR_DISCIPLINAS_ALUNO)))
          .addMethod(
            METHOD_INSERIR_MATRICULA,
            asyncUnaryCall(
              new MethodHandlers<
                InserirMatriculaRequest,
                InserirMatriculaResponse>(
                  this, METHODID_INSERIR_MATRICULA)))
          .build();
    }
  }

  /**
   * <pre>
   * interface de serviço
   * </pre>
   */
  public static final class GerenciadorDeNotasStub extends io.grpc.stub.AbstractStub<GerenciadorDeNotasStub> {
    private GerenciadorDeNotasStub(io.grpc.Channel channel) {
      super(channel);
    }

    private GerenciadorDeNotasStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GerenciadorDeNotasStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new GerenciadorDeNotasStub(channel, callOptions);
    }

    /**
     */
    public void listarAlunos(ListarAlunosRequest request,
        io.grpc.stub.StreamObserver<ListarAlunosResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_LISTAR_ALUNOS, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void alterarNota(AlterarNotaRequest request,
        io.grpc.stub.StreamObserver<AlterarNotaResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_ALTERAR_NOTA, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void alterarFaltas(AlterarFaltasRequest request,
        io.grpc.stub.StreamObserver<AlterarFaltasResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_ALTERAR_FALTAS, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void listarDisciplinasCurso(ListarDisciplinasCursoRequest request,
        io.grpc.stub.StreamObserver<ListarDisciplinasCursoResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_LISTAR_DISCIPLINAS_CURSO, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void listarDisciplinasAluno(ListarDisciplinasAlunoRequest request,
        io.grpc.stub.StreamObserver<ListarDisciplinasAlunoResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_LISTAR_DISCIPLINAS_ALUNO, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void inserirMatricula(InserirMatriculaRequest request,
        io.grpc.stub.StreamObserver<InserirMatriculaResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_INSERIR_MATRICULA, getCallOptions()), request, responseObserver);
    }
  }

  /**
   * <pre>
   * interface de serviço
   * </pre>
   */
  public static final class GerenciadorDeNotasBlockingStub extends io.grpc.stub.AbstractStub<GerenciadorDeNotasBlockingStub> {
    private GerenciadorDeNotasBlockingStub(io.grpc.Channel channel) {
      super(channel);
    }

    private GerenciadorDeNotasBlockingStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GerenciadorDeNotasBlockingStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new GerenciadorDeNotasBlockingStub(channel, callOptions);
    }

    /**
     */
    public ListarAlunosResponse listarAlunos(ListarAlunosRequest request) {
      return blockingUnaryCall(
          getChannel(), METHOD_LISTAR_ALUNOS, getCallOptions(), request);
    }

    /**
     */
    public AlterarNotaResponse alterarNota(AlterarNotaRequest request) {
      return blockingUnaryCall(
          getChannel(), METHOD_ALTERAR_NOTA, getCallOptions(), request);
    }

    /**
     */
    public AlterarFaltasResponse alterarFaltas(AlterarFaltasRequest request) {
      return blockingUnaryCall(
          getChannel(), METHOD_ALTERAR_FALTAS, getCallOptions(), request);
    }

    /**
     */
    public ListarDisciplinasCursoResponse listarDisciplinasCurso(ListarDisciplinasCursoRequest request) {
      return blockingUnaryCall(
          getChannel(), METHOD_LISTAR_DISCIPLINAS_CURSO, getCallOptions(), request);
    }

    /**
     */
    public ListarDisciplinasAlunoResponse listarDisciplinasAluno(ListarDisciplinasAlunoRequest request) {
      return blockingUnaryCall(
          getChannel(), METHOD_LISTAR_DISCIPLINAS_ALUNO, getCallOptions(), request);
    }

    /**
     */
    public InserirMatriculaResponse inserirMatricula(InserirMatriculaRequest request) {
      return blockingUnaryCall(
          getChannel(), METHOD_INSERIR_MATRICULA, getCallOptions(), request);
    }
  }

  /**
   * <pre>
   * interface de serviço
   * </pre>
   */
  public static final class GerenciadorDeNotasFutureStub extends io.grpc.stub.AbstractStub<GerenciadorDeNotasFutureStub> {
    private GerenciadorDeNotasFutureStub(io.grpc.Channel channel) {
      super(channel);
    }

    private GerenciadorDeNotasFutureStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected GerenciadorDeNotasFutureStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new GerenciadorDeNotasFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<ListarAlunosResponse> listarAlunos(
        ListarAlunosRequest request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_LISTAR_ALUNOS, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<AlterarNotaResponse> alterarNota(
        AlterarNotaRequest request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_ALTERAR_NOTA, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<AlterarFaltasResponse> alterarFaltas(
        AlterarFaltasRequest request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_ALTERAR_FALTAS, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<ListarDisciplinasCursoResponse> listarDisciplinasCurso(
        ListarDisciplinasCursoRequest request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_LISTAR_DISCIPLINAS_CURSO, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<ListarDisciplinasAlunoResponse> listarDisciplinasAluno(
        ListarDisciplinasAlunoRequest request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_LISTAR_DISCIPLINAS_ALUNO, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<InserirMatriculaResponse> inserirMatricula(
        InserirMatriculaRequest request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_INSERIR_MATRICULA, getCallOptions()), request);
    }
  }

  private static final int METHODID_LISTAR_ALUNOS = 0;
  private static final int METHODID_ALTERAR_NOTA = 1;
  private static final int METHODID_ALTERAR_FALTAS = 2;
  private static final int METHODID_LISTAR_DISCIPLINAS_CURSO = 3;
  private static final int METHODID_LISTAR_DISCIPLINAS_ALUNO = 4;
  private static final int METHODID_INSERIR_MATRICULA = 5;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final GerenciadorDeNotasImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(GerenciadorDeNotasImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_LISTAR_ALUNOS:
          serviceImpl.listarAlunos((ListarAlunosRequest) request,
              (io.grpc.stub.StreamObserver<ListarAlunosResponse>) responseObserver);
          break;
        case METHODID_ALTERAR_NOTA:
          serviceImpl.alterarNota((AlterarNotaRequest) request,
              (io.grpc.stub.StreamObserver<AlterarNotaResponse>) responseObserver);
          break;
        case METHODID_ALTERAR_FALTAS:
          serviceImpl.alterarFaltas((AlterarFaltasRequest) request,
              (io.grpc.stub.StreamObserver<AlterarFaltasResponse>) responseObserver);
          break;
        case METHODID_LISTAR_DISCIPLINAS_CURSO:
          serviceImpl.listarDisciplinasCurso((ListarDisciplinasCursoRequest) request,
              (io.grpc.stub.StreamObserver<ListarDisciplinasCursoResponse>) responseObserver);
          break;
        case METHODID_LISTAR_DISCIPLINAS_ALUNO:
          serviceImpl.listarDisciplinasAluno((ListarDisciplinasAlunoRequest) request,
              (io.grpc.stub.StreamObserver<ListarDisciplinasAlunoResponse>) responseObserver);
          break;
        case METHODID_INSERIR_MATRICULA:
          serviceImpl.inserirMatricula((InserirMatriculaRequest) request,
              (io.grpc.stub.StreamObserver<InserirMatriculaResponse>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static final class GerenciadorDeNotasDescriptorSupplier implements io.grpc.protobuf.ProtoFileDescriptorSupplier {
    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return HelloWorldProto.getDescriptor();
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (GerenciadorDeNotasGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new GerenciadorDeNotasDescriptorSupplier())
              .addMethod(METHOD_LISTAR_ALUNOS)
              .addMethod(METHOD_ALTERAR_NOTA)
              .addMethod(METHOD_ALTERAR_FALTAS)
              .addMethod(METHOD_LISTAR_DISCIPLINAS_CURSO)
              .addMethod(METHOD_LISTAR_DISCIPLINAS_ALUNO)
              .addMethod(METHOD_INSERIR_MATRICULA)
              .build();
        }
      }
    }
    return result;
  }
}
